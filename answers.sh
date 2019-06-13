#!/bin/bash
if [[ $# -eq 1 && -f $1 ]]; then
   input_file="${1}"
else
   input_file="test.txt"
fi

while read -r line
do
  x=$(echo $line | cut -d'x' -f1 | sed -e 's/^[ \t]*//g' -e 's/[ \t]*$//g')
  y=$(echo $line | cut -d'x' -f2 | cut -d= -f1 | sed -e 's/^[ \t]*//g' -e 's/[ \t]*$//g')
  result="$(echo $(( x * y )))"
  echo "$x x $y = $result"
done < ${input_file}
