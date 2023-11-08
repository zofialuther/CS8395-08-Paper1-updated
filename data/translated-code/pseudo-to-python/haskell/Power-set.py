def powerset(inputSet):
    return convertToSet(convertToList(inputSet))

def convertToList(inputSet):
    return list(inputSet)

def convertToSet(inputList):
    return set(inputList)

def listPowerset(inputList):
    return filterM(lambda x: [True, False], inputList)