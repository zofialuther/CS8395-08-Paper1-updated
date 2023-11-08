```python
from itertools import combinations

def ncsubs(L):
    LNCSL = set()
    for i in range(1, len(L) - 1):
        for combo in combinations(L[1:-1], i):
            LNCSL.add(combo)
    return LNCSL
```