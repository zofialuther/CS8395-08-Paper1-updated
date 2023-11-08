```python
from itertools import combinations

def disjoint(lst):
    pairs = list(combinations(lst, 2))
    disjoint_pairs = [pair for pair in pairs if pair[0] not in pair[1] and pair[1] not in pair[0]]
    return len(disjoint_pairs)

input_list = list(range(1, 21))
result = disjoint(input_list)
print(result)
```