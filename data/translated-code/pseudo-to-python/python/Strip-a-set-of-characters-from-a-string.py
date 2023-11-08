def stripchars(s, chars):
    result = ""
    for c in s:
        if c not in chars:
            result += c
    return result

s = "She was a soul stripper. She took my heart!"
chars = "aei"
print(stripchars(s, chars))