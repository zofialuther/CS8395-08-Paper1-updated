```python
from itertools import groupby
from operator import itemgetter

def extractRange(nums):
    ranges = []
    for k, g in groupby(enumerate(nums), lambda i_x: i_x[0] - i_x[1]):
        group = list(map(itemgetter(1), g))
        if len(group) > 1:
            ranges.append(f"{group[0]}-{group[-1]}")
        else:
            ranges.append(str(group[0]))
    return ','.join(ranges)
```