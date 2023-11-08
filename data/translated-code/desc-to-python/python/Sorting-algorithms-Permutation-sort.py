```python
from itertools import permutations
from more_itertools import windowed

def is_sorted(sequence):
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))

def permutation_sort(sequence):
    for perm in permutations(sequence):
        if is_sorted(perm):
            return perm
```