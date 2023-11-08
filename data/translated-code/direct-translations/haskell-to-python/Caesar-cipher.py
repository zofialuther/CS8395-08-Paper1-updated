```python
import string

def caesar(k, s):
    def addChar(b, o, c):
        b_ = ord(b)
        c_ = ord(c)
        return chr((b_ + (c_ - b_ + o) % 26))

    result = ""
    for char in s:
        if char.islower():
            result += addChar('a', k, char)
        elif char.isupper():
            result += addChar('A', k, char)
        else:
            result += char
    return result

def uncaesar(k, s):
    return caesar(-k, s)
```