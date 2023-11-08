Lowers = []

def char_type(char):
    return char.islower()

for c in maplist([alpha, ascii, lower]):
    if char_type(c):
        Lowers.append(c)

print('-- Lower Case Characters --')
print(Lowers)
print()

Uppers = []

def char_type(char):
    return char.isupper()

for c in maplist([alpha, ascii, upper]):
    if char_type(c):
        Uppers.append(c)

print('-- Upper Case Characters --')
print(Uppers)