```python
from itertools import product

def spellWith(blocks, word):
    if not word:
        return [[]]
    else:
        return [b + rest for b in blocks for rest in spellWith([x for x in blocks if x != b], word[1:]) if word[0].upper() in b]

blocks = ["BO", "XK", "DQ", "CP", "NA", "GT", "RE", "TG", "QD", "FS", "JW", "HU", "VI", "AN", "OB", "ER", "FS", "LY", "PC", "ZM"]

testCases = ["", "A", "BARK", "BoOK", "TrEAT", "COmMoN", "SQUAD", "conFUsE"]

for testCase in testCases:
    print((not not spellWith(blocks, testCase.upper()), testCase))
```