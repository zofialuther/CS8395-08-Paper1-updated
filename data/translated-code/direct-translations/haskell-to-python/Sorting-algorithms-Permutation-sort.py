```python
from itertools import permutations

def permutation_sort(l):
    return next(p for p in permutations(l) if is_sorted(p))

def is_sorted(p):
    return all(p[i] <= p[i+1] for i in range(len(p)-1))

def permute(l):
    result = []
    for e in l:
        result = [p[:i] + (e,) + p[i:] for p in result for i in range(len(p)+1)]
    return result

```