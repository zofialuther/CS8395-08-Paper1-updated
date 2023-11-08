```python
from itertools import groupby

def isCollapsible(s):
    return any(len(list(group)) > 1 for key, group in groupby(s))

def collapsed(s):
    return ''.join(key for key, group in groupby(s))
```