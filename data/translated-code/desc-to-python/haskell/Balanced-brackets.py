```python
import random

def shuffle(lst, rng):
    n = len(lst)
    for i in range(n-1, 0, -1):
        j = rng.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst
```