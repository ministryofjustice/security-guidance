#!/bin/sh
git ls-tree -r --name-only HEAD | grep "\.dita$" | while read filename; do
	echo "$(git log -1 --date=iso-strict --format='%ad' -- $filename) $filename"
done | sort --reverse
