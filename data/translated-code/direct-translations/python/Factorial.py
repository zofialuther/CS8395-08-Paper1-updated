```python
from itertools import accumulate, chain
from operator import mul

def factorial(n):
    return list(
        accumulate(chain([1], range(1, 1 + n)), mul)
    )[-1]
```