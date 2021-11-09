# Strip out HTML tags,
# and flow text,
# to simplify file comparison.

# Usage: python addLinkTarget.py infile

import os
import re
import sys

reportFile = sys.argv[1];
print("Processing "+reportFile)
inFile=open(reportFile, 'r')
outFile=open(reportFile+".new",'a')
for line in inFile:
    if(line.startswith("##")):
        # We've found a heading, so add an HTML target.
        # Work out what the heading ID should be.
        # Begin by removing the Markdown heading tag.
        working = re.sub('^#+\s+', '', line)
        # Remove all whitespace from end of the line.
        working = re.sub('\s+$', '', working)
        # Remove question marks
        working = re.sub('\?', '', working)
        # Remove ampersands
        working = re.sub('\&', '', working)
        # Remove commas
        working = re.sub(',', '', working)
        # Remove back-ticks
        working = re.sub('\`', '', working)
        # Remove single-quotes
        working = re.sub('\'', '', working)
        # Convert spaces to dashes
        working = re.sub('\s', '-', working)
        # Convert strokes to dashes
        working = re.sub('\/', '-', working)
        # Convert multiple dashes to single dash
        working = re.sub('[-]+', '-', working)
        # Convert to lowercase
        working = working.lower()
        # Add horizontal dash for Intranet compliance.
        if working == "feedback":
            outFile.write("---\n\n")
        # outFile.write("<a id=\""+working+"\"></a>\n\n")
    # Now remove escaped brackets.
    working = line.replace("\(", "(")
    working = working.replace("\)", ")")
    # Remove escaped angle-brackets.
    working = working.replace("\>", ">")
    # Remove hard-coded file prefix.
    working = working.replace("file:///", "")
    # Remove hard-coded intranet link.
    working = working.replace("https://intranet.justice.gov.uk", "")
    # Redirect links to security-guidance.
    while(".md" in working):
        # print "Found: "+working
        working = re.sub('\]\((\S+)\.md','](https://security-guidance.service.justice.gov.uk/\g<1>/',working);
        # print "Now:   "+working
    # Convert markdown heading tag to level 2 (always).
    # working = re.sub("^(?P<hashes>#+)\s+", "\g<hashes>", working)
    # Best practice is to leave a space after the hashes:
    #  https://www.markdownguide.org/basic-syntax#heading-best-practices
    # Intranet does not accept spaces after hashes.
    working = re.sub("^#\s+", "#", working)
    working = re.sub("^##+\s+", "##", working)
    # Change bullet list indicator.
    working = re.sub("^\-\s+", "* ", working)
    # Change bullet sub-list indicator.
    working = re.sub("^\s\s\s\s\-\s+", "    * ", working)
    outFile.write(working)
outFile.close
inFile.close
os.remove(reportFile)
os.rename(reportFile+".new",reportFile)
