def checkSuffix(string, suffix):
    lengthOfString = len(string)
    lengthOfSuffix = len(suffix)
    compareString = string[lengthOfString - lengthOfSuffix:]
    if compareString == suffix:
        return True
    else:
        return False