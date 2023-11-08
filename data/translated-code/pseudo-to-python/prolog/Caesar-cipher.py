```python
from clpfd import *

def caesar(Key, L1, L2):
    L2 = caesar_cipher(Key, L1)

L1 = "The five boxing wizards jump quickly"
print("Original : %s\n" % L1)
caesar(3, L1, L2)
print("Encoding : %s\n" % L2)
caesar(3, L3, L2)
print("Decoding : %s\n" % L3)

def encoding(Key, L1, L2):
    L2 = list(map(lambda x: caesar_cipher(Key, x), L1))

def caesar_cipher(V1, V2):
    V2 = V1 + V2
    A = ((V1 <= 'Z' and V2 > 'Z') or (V1 <= 'z' and V2 > 'z') or (V1 < 'A' and V2 >= 'A') or (V1 < 'a' and V2 >= 'a')) ==> A
    V2 = V - A * 26
    label([A, V1, V2])
```