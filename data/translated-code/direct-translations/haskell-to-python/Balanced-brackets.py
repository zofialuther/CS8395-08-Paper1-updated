```python
import random
import numpy as np

def pairs(l, u, r):
    result = []
    for i in range(l, u):
        j = random.randint(i, u)
        result.append((i, j))
    return result

def shuffle(xs, r):
    v = np.array(xs)
    p = pairs(0, len(v) - 1, r)
    for i, j in p:
        v[i], v[j] = v[j], v[i]
    return list(v)
```