```python
import itertools
import more_itertools

def is_sorted(sequence):
    for pair in more_itertools.windowed(sequence, 2):
        if pair[0] > pair[1]:
            return False
    return True

def permutation_sort(sequence):
    for perm in itertools.permutations(sequence):
        if is_sorted(perm):
            return perm
```