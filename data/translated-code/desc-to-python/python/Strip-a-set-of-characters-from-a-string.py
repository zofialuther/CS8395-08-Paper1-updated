def stripchars(s, chars):
    return ''.join([char for char in s if char not in chars])

result = stripchars("She was a soul stripper. She took my heart!", "aei")
print(result)