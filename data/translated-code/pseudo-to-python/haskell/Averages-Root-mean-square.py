```python
from functools import reduce
import math

def rootMeanSquare(lst):
    result = math.sqrt(reduce(lambda acc, x: acc + x**2, lst, 0) / len(lst)
    return result

def main():
    print(rootMeanSquare(list(range(1, 11)))
```