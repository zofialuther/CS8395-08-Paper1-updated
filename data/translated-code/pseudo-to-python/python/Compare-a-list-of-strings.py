def allEqual(strings):
    for i in range(len(strings) - 1):
        if strings[i] != strings[i+1]:
            return False
    return True

def strictlyAscending(strings):
    for i in range(len(strings) - 1):
        if strings[i] >= strings[i+1]:
            return False
    return True

def conciseAllEqual(strings):
    uniqueStrings = set(strings)
    if len(uniqueStrings) == 1:
        return True
    else:
        return False

def conciseAscending(strings):
    sortedStrings = sorted(strings, reverse=True)
    if sortedStrings == strings:
        return True
    else:
        return False

# Main code
strings = ["abc", "def", "ghi"]
if allEqual(strings) is True:
    print("All strings are equal")
if strictlyAscending(strings) is True:
    print("Strings are strictly ascending")
if conciseAllEqual(strings) is True:
    print("Concise: All strings are equal")
if conciseAscending(strings) is True:
    print("Concise: Strings are ascending")