```python
import numpy as np
from numpy import random

def disSort1(xs, is_):
    is_ = np.sort(is_)
    sub = [(i, xs[i]) for i in range(len(xs)) if i in is_]
    rest = [xs[i] for i in range(len(xs)) if i not in is_]
    sub_sorted = sorted(sub, key=lambda x: x[0])
    merged = rest + [x[1] for x in sub_sorted]
    return merged

def disSort2(xs, is_):
    as_ = np.array(xs)
    sub = [(i, as_[i]) for i in is_]
    sub_sorted = sorted(sub, key=lambda x: x[0])
    as_[is_] = [x[1] for x in sub_sorted]
    return list(as_)

def disSort3(xs, is_):
    as_ = np.array(xs)
    sub = [(i, as_[i]) for i in is_]
    sub_sorted = sorted(sub, key=lambda x: x[0])
    for i, val in sub_sorted:
        as_[i] = val
    return list(as_)

xs = [7, 6, 5, 4, 3, 2, 1, 0]
is_ = [6, 1, 7]
print(disSort1(xs, is_))
print(disSort2(xs, is_))
print(disSort3(xs, is_))
```