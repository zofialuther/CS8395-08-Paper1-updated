```python
from random import random
from functools import reduce
import matplotlib.pyplot as plt

def f1(p):
    x, y = p
    return (0, 0.16 * y)

def f2(p):
    x, y = p
    return (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)

def f3(p):
    x, y = p
    return (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6)

def f4(p):
    x, y = p
    return (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)

def func(p, r):
    if r < 0.01:
        return f1(p)
    elif r < 0.86:
        return f2(p)
    elif r < 0.93:
        return f3(p)
    else:
        return f4(p)

def fern(rs):
    return reduce(lambda acc, r: acc + [func(acc[-1], r)], rs, [(0, 0)])

def drawFern(rs, n):
    points = fern(rs)[:n]
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.scatter(x, y, color='green', s=1)
    plt.show()

drawFern([random() for _ in range(10000)], 10000)
```