def divide(num1, num2):
    listToReturn =[]
    for x in range(num1, num2):
        if(x%7==0) and (x%5!=0):
            listToReturn.append(x)
    return listToReturn

a =int(input("Enter first number: ")) 
b = int(input("Enter second number: "))
numToReturn = divide(a, b)
print(numToReturn)
