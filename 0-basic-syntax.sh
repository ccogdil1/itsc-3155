#!/BIN/BASHSHELL

class = "ITIS 3246"
echo "Welcome to $class"

if [[ -z $1 ]]
  then
  echo "Please tell me your name by running the script this way:"
  echo "$0 <name>"
  exit -1
end

echo "Hi $1"

for x in foo bar baz  
  echo "$x is a common variable name in CS assignments"