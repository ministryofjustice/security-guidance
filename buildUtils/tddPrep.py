# Strip out HTML tags,
# and flow text,
# to simplify file comparison.

# Usage: python tddPrep.py < infile.html > outfile.html

import re
import sys

for line in sys.stdin:
    # Get rid of the eol character.
    working = line.rstrip()
    # Strip out fully formed HTML tags.
    working = re.sub('<[^>]+>', ' ', working)
    # Remove all whitespace from start of the line.
    working = re.sub('^\s+', '', working)
    # Remove all whitespace from end of the line.
    working = re.sub('\s+$', '', working)
    # Convert multiple whitespace to single space character.
    working = re.sub('\s+', ' ', working)
    # Convert HTML ampersand character.
    working = re.sub('&amp;', '&', working)
    # Separate each word in the line to its own line.
    working = re.sub('\s', '\n', working)
    # If there's anything left, print it out.
    if (working !=""):
        print(working)
