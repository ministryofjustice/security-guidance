# Strip out HTML tags,
# and flow text,
# to simplify file comparison.

# Usage: python addLinkTarget.py infile

import re
import sys

def check_parm():
        arguments = sys.argv[1:]
        count = len(arguments)
        if count < 1:
                print("\n")
                print("addLinkTarget tool can be run using:\n")
                print("[PROGRAM NAME] [FILE]")
                sys.exit();

check_parm();
reportFile = sys.argv[1];
print("Processing "+reportFile)
inFile=open(reportFile, 'r')
outFile=open(reportFile+".new",'a')
for line in inFile:
    if(line.startswith("##")):
        # We've found a heading, so add an HTML target.
        # Work out what the heading ID should be.
        # Begin by removing the Markdown heding tag.
        working = re.sub('^#+\s+', '', line)
        # Remove all whitespace from end of the line.
        working = re.sub('\s+$', '', working)
        # Remove question marks
        working = re.sub('\?', '', working)
        # Remove ampersands
        working = re.sub('\&', '', working)
        # Convert spaces to dashes
        working = re.sub('\s', '-', working)
        # Convert multiple dashes to single dash
        working = re.sub('[-]+', '-', working)
        # Convert to lowercase
        working = working.lower()
        outFile.write("<a id=\""+working+"\"></a>\n")
    # Now remove escaped brackets.
    working = re.sub('[\\][\(]', '+', line)
    working = re.sub('[\\][\)]', '+', working)
    outFile.write(working)
outFile.close
inFile.close