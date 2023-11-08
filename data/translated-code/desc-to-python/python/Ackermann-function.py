```python
from functools import lru_cache

@lru_cache(maxsize=None)
def ack2(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack2(m - 1, 1)
    else:
        return ack2(m - 1, ack2(m, n - 1))
```