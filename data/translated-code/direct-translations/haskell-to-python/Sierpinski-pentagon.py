```python
from functools import reduce

def scale(s):
    return lambda x: (x[0]*s, x[1]*s)

def rotate(angle):
    return lambda x: (x[0]*math.cos(math.radians(angle)) - x[1]*math.sin(math.radians(angle)), x[0]*math.sin(math.radians(angle)) + x[1]*math.cos(math.radians(angle)))

def copy(angle):
    return lambda x: (x[0]*math.cos(math.radians(angle)) - x[1]*math.sin(math.radians(angle)), x[0]*math.sin(math.radians(angle)) + x[1]*math.cos(math.radians(angle)))

def foldMap(func, lst):
    return reduce(lambda x, y: func(y)(x), lst, (1,1))

s = 2
transformation = scale(s)(rotate(36)(foldMap(copy, [0,72,144,216,288])))
```