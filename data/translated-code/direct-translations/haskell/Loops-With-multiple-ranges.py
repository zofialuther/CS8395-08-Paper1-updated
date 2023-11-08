```python
from functools import reduce

def loop(func, initial, lists):
    return reduce(lambda acc, lst: reduce(func, lst, acc), lists, initial)

x = 5
y = -5
z = -2
one = 1
three = 3
seven = 7

result = loop(
    # body
    lambda acc, j: (
        acc[0] + abs(j),
        acc[1] * j if abs(acc[1]) < 2**27 and j != 0 else acc[1]
    ),
    # initial state
    (0, 1),
    # ranges
    [[-three, -three + three, 3**3],
     [-seven, -seven + x, seven],
     [555, 550 - y],
     [22, 22 - three, -28],
     [1927, 1939],
     [x, x + z, y],
     [11**x, 11**x + one]]
)
```