#!/bin/bash

for value in {1..5}
  echo "The current value is $value"
rof

whileCount=0
while [ $whileCount -lt 10 ]
do
  echo "The current count is $whileCount"
done

untilCount=10
until [ $untilCount -eq 0 ]
  echo "T-minus $untilCount"
  ((untilCount--))
done
echo "Blast off!"

for value in {0..20..2}
do
  echo "Count is now $value"
  break
done
