#!/bin/bash

# Run from within the buildUtils folder:
# bash ./checkSpelling.sh

function preprocess {
#  tr '\n' ' ' | tr '#' ' ' | tr '*' ' ' | perl -pe 's|---.*?---||g' | tr '-' ' ' | perl -pe 's|```.*?```||g' | perl -pe 's|<script.*?</script>||g' | perl -pe 's|&nbsp;||g' | perl -pe 's|&lt;||g' | perl -pe 's|&gt;||g' | perl -pe 's|<code.*?</code>||g' | perl -pe 's|<form.*?</form>||g' | perl -pe 's|<style.*?</style>||g' | perl -pe 's|<[/a-zA-Z].*?>||g' | perl -pe 's|`.*?`||g' | perl -pe 's|]\(.*?\)| |g'
  tr '\n' ' ' | tr '#' ' ' | tr '*' ' ' | perl -pe 's|---.*?---||g' | perl -pe 's|```.*?```||g' | perl -pe 's|&nbsp;||g' | perl -pe 's|&lt;||g' | perl -pe 's|&gt;||g' | perl -pe 's|<code.*?</code>||g' | perl -pe 's|<[/a-zA-Z].*?>||g' | perl -pe 's|`.*?`||g' | perl -pe 's|]\(.*?\)| |g' | perl -pe 's|]\[.*?\]| |g' | perl -pe 's|\[.*?\]\:\s+http[^\s]+| |g' | perl -pe 's|[\|\[]| |g' | tr '-' ' ' | sed "s/\\\(/\(/g" | sed "s/\\\)/\)/g"
}

function checkFile {
  cat "$1" | preprocess | aspell -a --encoding=utf-8 --lang=en-gb --add-extra-dicts="./localDictionary.en.pws" | grep -v '^[\*@]' | grep -v '^$' | cut -f2 -d ' '
}

function changedFiles {
  find ../docs ../intranet/ost ../ktt -iname "*.md"
}

function check {
  while read file; do
    echo
    echo "Checking $file"
    echo "=============="
    for word in `checkFile "$file"`; do
      echo "$word"
    done
  done
}

# changedFiles

report="$(changedFiles . | sort | check )"

if [[ "$(echo -n "$report" | grep -v '^==============$' | grep -v '^Checking ')" = '' ]]; then
  echo "==================="
  echo "Spell check passed."
  echo "==================="
  exit 0;
else
  echo "$report"
  exit 1;
fi

exit 0;
