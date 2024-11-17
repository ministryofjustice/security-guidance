# Add markdown targets for definition list entries

# Usage: python dlTarget.py infile

import os
import re
import sys

reportFile = sys.argv[1];
print("Processing "+reportFile)
inFile=open(reportFile, 'r')
outFile=open(reportFile+".new",'a')
for line in inFile:
    working = line.strip()
    if(working.startswith("-   **") and working.endswith("**")):
        # We've found a definition list entry.
        # Work out what the target ID should be.
        # Begin by removing the start of the entry.
        working = re.sub(r'^-\s\s\s\*\*', '', working)
        # Remove the end of the entry.
        working = re.sub(r'\*\*$', '', working)
        # Remove question marks
        working = re.sub(r'\?', '', working)
        # Remove ampersands
        working = re.sub(r'\&', '', working)
        # Remove commas
        working = re.sub(r',', '', working)
        # Remove back-ticks
        working = re.sub(r'\`', '', working)
        # Remove single-quotes
        working = re.sub(r'\'', '', working)
        # Convert spaces to dashes
        working = re.sub(r'\s', '-', working)
        # Convert strokes to dashes
        working = re.sub(r'\/', '-', working)
        # Convert multiple dashes to single dash
        working = re.sub(r'[-]+', '-', working)
        # Convert to lowercase
        working = working.lower()
        # Now remove escaped brackets.
        working = working.replace(r"\(", "")
        working = working.replace(r"\)", "")
        # Remove escaped angle-brackets.
        working = working.replace(r"\<", "")
        working = working.replace(r"\>", "")
        # Ready to output.
        # Output the newly created HTML target tag
        outFile.write("<a name=\""+working+"\"></a>\n\n")
    # Lastly, output the original line
    outFile.write(line)
outFile.close
inFile.close
os.remove(reportFile)
os.rename(reportFile+".new",reportFile)
