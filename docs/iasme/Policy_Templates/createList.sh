#!/bin/bash

echo "# IASME templates" > index.md
echo "" >> index.md
for i in *
do
	label=`sed 's/_TEMPLATE_V1//; s/_GUIDELINES_V1//; s/_/ /g; s/.docx//; s/.odt//; s/.ods//; s/.xlsx//' <(echo "$i")`
	echo "[$label TEMPLATE]($i)" >> index.md
done
