def allEqual(strings):
    stringA = strings[0]
    for string in strings:
        if string != stringA:
            return False
    return True