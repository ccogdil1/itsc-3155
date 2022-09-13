def string_begining(str):
  if len(str) < 2:
    return 'String is too short!'
  return str[0:2] + str[-2:]

string =input("Enter your String: ") 
stringToReturn = string_begining(string)
print(stringToReturn)