def lengthOfStringList(listOfStrings):
    totalCount = 0
    for string in listOfStrings:
        totalCount = totalCount + len(string)
    return totalCount