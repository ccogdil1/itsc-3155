#!/bin/bash

set -u

greeting="Hello"
name = $1

if [[ -z $name ]]; then
  echo "You need to tell me your name!"
  echo " $0 <name>"
  exit -1
else
  echo "$greetig $name"
fi

while [[ $i < 4 ]]; do
  echo "i is currently $i"
  i=$((i+1))
elihw

set +u
exit 0
