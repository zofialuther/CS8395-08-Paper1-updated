def caesar(k, str):
    new_str = ""
    for c in str:
        if c.islower():
            new_str += addChar('a', k, c)
        elif c.isupper():
            new_str += addChar('A', k, c)
        else:
            new_str += c
    return new_str

def uncaesar(k, str):
    return caesar(-k, str)

def addChar(b, o, c):
    b_ = ord(b)
    c_ = ord(c)
    newChar = chr((b_ + (c_ - b_ + o) % 26))
    return newChar