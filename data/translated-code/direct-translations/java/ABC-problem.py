```python
def canMakeWord(word, blocks):
    if not word:
        return True
    
    c = word[0]
    for i in range(len(blocks)):
        b = blocks[i]
        if c not in b:
            continue
        blocks[0], blocks[i] = blocks[i], blocks[0]
        if canMakeWord(word[1:], blocks[1:]):
            return True
        blocks[0], blocks[i] = blocks[i], blocks[0]
    
    return False

blocks = ["BO", "XK", "DQ", "CP", "NA",
          "GT", "RE", "TG", "QD", "FS",
          "JW", "HU", "VI", "AN", "OB",
          "ER", "FS", "LY", "PC", "ZM"]

words = ["", "A", "BARK", "BOOK", "TREAT", "COMMON", "SQUAD", "CONFUSE"]
for word in words:
    print(f"{word if word else '\"\"'}: {canMakeWord(word, blocks)}")
```