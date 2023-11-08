```python
from prologpy import *

def caesar():
    L1 = "The five boxing wizards jump quickly"
    print("Original : %s" % L1)

    # encryption of the sentence
    L2 = encoding(3, L1)
    print("Encoding : %s" % L2)

    # deciphering on the encoded sentence
    L3 = encoding(3, L2)
    print("Decoding : %s" % L3)

# encoding/decoding of a sentence
def encoding(Key, L1):
    L2 = [caesar_cipher(Key, char) for char in L1]
    return ''.join(L2)

def caesar_cipher(Key, char):
    if char == ' ':
        return ' '

    V1 = ord(char) - (ord('A') if char.isupper() else ord('a'))
    V = Key + V1
    A = 1 if (ord(char) <= ord('Z') and V > ord('Z')) or (ord(char) <= ord('z') and V > ord('z')) or (ord(char) < ord('A') and ord(char) >= ord('A')) or (ord(char) < ord('a') and ord(char) >= ord('a')) else 0
    V2 = V - A * 26
    return chr(V2 + (ord('A') if char.isupper() else ord('a')))

caesar()
```