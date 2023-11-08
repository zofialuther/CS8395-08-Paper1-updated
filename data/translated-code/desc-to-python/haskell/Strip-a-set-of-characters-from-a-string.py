def stripChars(string1, string2):
    return ''.join(filter(lambda x: x not in string2, string1))