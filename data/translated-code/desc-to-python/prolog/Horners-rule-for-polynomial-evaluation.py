```python
from hiordlib import foldr

def horner(L, X, Result):
    return foldr(lambda coefficient, acc: coefficient + X * acc, L, Result)
```