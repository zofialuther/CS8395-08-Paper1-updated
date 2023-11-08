def stripChars(str, chars):
    result = ''.join(filter(lambda char: char not in chars, str))
    return result