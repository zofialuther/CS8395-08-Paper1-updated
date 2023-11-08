```python
from itertools import chain, combinations

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
```