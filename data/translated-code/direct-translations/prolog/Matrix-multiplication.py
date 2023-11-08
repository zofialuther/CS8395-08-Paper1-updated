```python
from itertools import starmap

def dot(v1, v2):
    return sum(starmap(lambda x, y: x * y, zip(v1, v2)))

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def mmult(m1, m2):
    m2t = transpose(m2)
    return [[dot(row, col) for col in m2t] for row in m1]
```