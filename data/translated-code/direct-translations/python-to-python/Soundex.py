def soundex(word):
    word = word.lower()
    mapping = {
        'b': 1, 'f': 1, 'p': 1, 'v': 1,
        'c': 2, 'g': 2, 'j': 2, 'k': 2, 'q': 2, 's': 2, 'x': 2, 'z': 2,
        'd': 3, 't': 3,
        'l': 4,
        'm': 5, 'n': 5,
        'r': 6
    }
    
    result = word[0].upper()
    prev_code = 0
    for char in word[1:]:
        code = mapping.get(char, 0)
        if code != prev_code and code != 0:
            result += str(code)
        prev_code = code
    result = result + "000"
    return result[:4]

print(soundex("soundex"))
print(soundex("example"))
print(soundex("ciondecks"))
print(soundex("ekzampul"))