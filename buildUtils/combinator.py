# Python script to replace first page of content file
# with a supplied cover page file.
# Then to add the last page from the cover file.
# Output goes into a named file.
# All files are PDFs.

# Run as:
#	python3 combinator.py <cover_file> <content_file> <output_file>
# For example:
#	python3 combinator.py cover.pdf content.pdf out.pdf

# This code depends on the PyPDF2 package.
# Install the package beforehand using:
#	python3 -m pip install PyPDF2
# Verify that the install worked by running:
#	python3 -m pip show PyPDF2

# Load requiredlibraries.
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# Create a path object to point to the incoming cover file.
pdf_cover = (
	Path.cwd()
	/ sys.argv[1]
)
# Create a path object to point to the incoming content file.
pdf_content = (
	Path.cwd()
	/ sys.argv[2]
)

# Prepare to store the assembled content.
pdf_writer = PdfFileWriter()

# Get ready to read the first page (only) of the cover file.
cover_pdf = PdfFileReader(str(pdf_cover))
# Read just the first page...
for page in cover_pdf.pages[0:1]:
	# ... and add that single page into our assembly file.
	pdf_writer.addPage(page)

# Get ready to read all pages of the cover file,
# except for the first page (which we are replacing
# with the supplied cover file.
content_pdf = PdfFileReader(str(pdf_content))
# Read all pages except the first page (ie page 0)...
for page in content_pdf.pages[1:]:
	# ... and add each page to the assembly output file.
	pdf_writer.addPage(page)

# Now read the last page of the cover...
for page in cover_pdf.pages[-2:-1]:
	# ... and add that single page into our assembly file.
	pdf_writer.addPage(page)

# Finally, output the complete assembled file.
with Path(sys.argv[3]).open(mode="wb") as output_file:
	pdf_writer.write(output_file)
