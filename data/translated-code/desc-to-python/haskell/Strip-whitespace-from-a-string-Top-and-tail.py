```python
from Data.List import dropWhile, dropWhileEnd

def trimLeft(s):
    return dropWhile(lambda c: c.isspace(), s)

def trimRight(s):
    return dropWhileEnd(lambda c: c.isspace(), s)

def trim(s):
    return trimLeft(trimRight(s))
```