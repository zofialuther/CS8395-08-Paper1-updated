def stripChars(chars_to_strip, string):
    return ''.join(filter(lambda c: c not in chars_to_strip, string))