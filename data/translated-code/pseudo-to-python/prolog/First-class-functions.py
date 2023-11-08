```python
from math import sin, cos, asin, acos

def compose(F, G):
    return lambda X, Z: (G(X), F(Z))

def cube(X):
    return X ** 3

def cube_root(X):
    return X ** (1/3)

def first_class():
    L = [sin, cos, cube]
    IL = [asin, acos, cube_root]

    # we create the composed functions
    Lst = list(map(compose, L, IL))

    # we call the functions
    R = list(map(lambda x: x[0](0.5, x[1](0.5)), Lst))

    # we display the results
    for r in R:
        print(r)
```