def mergeDict(first, second):
    return(second.update(first))    
    
firstDict = {'a': 100, 'b': 200, 'c': 300}
secondDict = {'a': 300, 'b': 200, 'd': 400}

mergeDict(firstDict, secondDict)

print(secondDict)