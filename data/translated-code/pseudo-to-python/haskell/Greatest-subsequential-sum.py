```python
from itertools import combinations

def subseqs(arr):
    result = []
    for i in range(len(arr)+1):
        result.extend(list(combinations(arr, i)))
    return result

def maxsubseq(arr):
    subseq = subseqs(arr)
    max_sum = float('-inf')
    max_subseq = []
    for s in subseq:
        if sum(s) > max_sum:
            max_sum = sum(s)
            max_subseq = s
    return list(max_subseq)

print(maxsubseq([-1, -2, 3, 5, 6, -2, -1, 4, -4, 2, -1]))
```