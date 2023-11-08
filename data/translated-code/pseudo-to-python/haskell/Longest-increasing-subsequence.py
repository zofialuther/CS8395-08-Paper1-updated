```python
from functools import cmp_to_key
import itertools

def isSorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def lis(arr):
    subsequences = [list(x) for x in itertools.chain.from_iterable(itertools.combinations(arr, r) for r in range(len(arr)+1))]
    sorted_subsequences = filter(isSorted, subsequences)
    unique_subsequences = map(list, set(map(tuple, sorted_subsequences)))
    return max(unique_subsequences, key=len)

print(lis([3,2,6,4,5,1]))
print(lis([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))
print(lis([1,1,1,1]))
```