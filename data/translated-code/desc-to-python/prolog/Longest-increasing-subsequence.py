```python
from itertools import combinations
from functools import reduce

def increasing_subsequences(lst):
    return reduce(lambda result, ele: result + [subseq + [ele] for subseq in result if not subseq or subseq[-1] < ele], lst, [[]])

def lis(lst, Out):
    subs = increasing_subsequences(lst)
    max_len = max(len(sub) for sub in subs)
    longest_subs = [sub for sub in subs if len(sub) == max_len]
    Out = list(reversed(longest_subs[0]))
```