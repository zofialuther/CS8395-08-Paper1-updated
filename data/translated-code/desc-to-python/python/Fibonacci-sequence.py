```python
from functools import reduce
import operator

def nthFib(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return reduce(lambda x, _: (x[1], x[0] + x[1]), range(2, n), (0, 1))[1]

print(nthFib(1000))
```