```python
import itertools

def all_subsequences(arr):
    return [list(sub) for sub in itertools.chain.from_iterable(itertools.combinations(arr, r) for r in range(len(arr) + 1))]

def max_subsequence(arr):
    max_sum = float('-inf')
    result = []
    for subseq in all_subsequences(arr):
        subseq_sum = sum(subseq)
        if subseq_sum > max_sum:
            max_sum = subseq_sum
            result = subseq
    return result

specific_list = [1, -3, 4, -2, -1, 6]
print(max_subsequence(specific_list))
```