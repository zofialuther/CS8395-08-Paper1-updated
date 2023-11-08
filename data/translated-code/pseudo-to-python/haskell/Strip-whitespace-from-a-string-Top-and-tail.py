```python
from Data.Char import isSpace
from Data.List import dropWhileEnd

def trimLeft(s):
    return dropWhile(isSpace, s)

def trimRight(s):
    return dropWhileEnd(isSpace, s)

def trim(s):
    return trimLeft(trimRight(s))
```