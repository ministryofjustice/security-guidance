#!/bin/bash

# Warn of any instances of avoid words
# (https://www.gov.uk/guidance/style-guide/a-to-z-of-gov-uk-style#words-to-avoid).

# Run from within the buildUtils folder:
# sh ./detectAvoidWords.sh

# Also added avoid words, to improve accessibility:
#  above
#  below

declare -a avoidList=(
  "above"
  "agenda"
  "advancing"
  "below"
  "collaborate"
  "combating"
  "commit"
  "countering"
  "deliver"
  "deploy"
  "dialogue"
  "disincentivise"
  "drive"
  "empower"
  "facilitate"
  "focusing"
  "foster"
  "going\ forward"
  "impact"
  "incentivise"
  "initiate"
  "in\ order\ to"
  "key"
  "land"
  "leverage"
  "liaise"
  "one-stop\ shop"
  "overarching"
  "pledge"
  "progress"
  "promote"
  "ring\ fencing"
  "robust"
  "slim"
  "streamline"
  "strengthening"
  "tackling"
  "transforming"
  "utilise"
)

function changedFiles {
  find ../docs -iname "*.md"
}

function check {
  while read file; do
    echo
    echo "Checking for avoid words in $file"
    echo "=============="
    for word in "${avoidList[@]}"; do
      if [[ "$(cat "$file" | sed "s/\\\(/\(/g" | sed "s/\\\)/\)/g" | grep -ic $word 2> /dev/null)" > 0 ]]; then
        echo $word
      fi
    done
  done
}

changedFiles . | sort | check

exit 0
