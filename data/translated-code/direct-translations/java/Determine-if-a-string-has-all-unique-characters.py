```python
words = ["", ".", "abcABC", "XYZ ZYX", "1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ"]

for word in words:
    seen = set()
    first = next((ch for ch in map(ord, word) if ch in seen), None)
    if first is not None:
        ch = chr(first)
        hex_val = hex(first).upper()
        print(f"Word: \"{word}\" contains a repeated character.")
        print(f"Character '{ch}' (hex {hex_val}) occurs at positions {word.index(ch)} and {word.index(ch, word.index(ch) + 1)}")
    else:
        print(f"Word: \"{word}\" has all unique characters.")
    print()
```