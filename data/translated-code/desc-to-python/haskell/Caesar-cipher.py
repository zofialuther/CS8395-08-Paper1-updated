```python
# Caesar.py

def caesar(k, s):
    result = ""
    for char in s:
        result += addChar(char, k)
    return result

def uncaesar(k, s):
    result = ""
    for char in s:
        result += addChar(char, -k)
    return result

def addChar(c, k):
    if c.isalpha():
        shift = (ord(c) - 65 + k) % 26 + 65 if c.isupper() else (ord(c) - 97 + k) % 26 + 97
        return chr(shift)
    else:
        return c
```