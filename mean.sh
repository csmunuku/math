#!/bin/bash
usage()
{
  echo "See the usage below:"
  echo "$0 2 3 4"
  echo "$0 5 8 9"
  exit 0
}
mean()
{
  meanCount=0
  numbers=$(echo $* | tr -s ',' ' ')
  count=0
  for i in $numbers
  do
    ((meanCount = meanCount + $i))
    ((count = count + 1))
  done
  (( result = meanCount/count ))
  echo $result
}

if [ $# -gt 0 ]; then
   mean $*
else
   usage
fi
