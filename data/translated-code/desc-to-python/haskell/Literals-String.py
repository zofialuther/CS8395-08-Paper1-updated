```python
string1 = "abcdef"
string2 = "abc\def"
string3 = "abc\ndef"
string4 = "abc\n\def"

if string1 == string2:
    print("String 1 and String 2 are equivalent")
else:
    print("String 1 and String 2 are not equivalent")

if string3 == string4:
    print("String 3 and String 4 are equivalent")
else:
    print("String 3 and String 4 are not equivalent")
```