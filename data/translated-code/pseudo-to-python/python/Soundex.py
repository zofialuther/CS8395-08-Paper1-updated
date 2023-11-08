def soundex(word):
    word = word.upper()
    code = word[0]
    mapping = {
        "BFPV": "1",
        "CGJKQSXZ": "2",
        "DT": "3",
        "L": "4",
        "MN": "5",
        "R": "6"
    }
    for char in word[1:]:
        for key in mapping:
            if char in key:
                digit = mapping[key]
                if digit != code[-1]:
                    code += digit
    while len(code) < 4:
        code += "0"
    return code[:4]

print(soundex("soundex"))
print(soundex("example"))
print(soundex("ciondecks"))
print(soundex("ekzampul"))