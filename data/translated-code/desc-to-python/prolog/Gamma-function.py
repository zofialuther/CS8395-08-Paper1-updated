```python
import math

def gamma(X, Y):
    if X < 0:
        return math.nan
    elif X < 0.5:
        return math.pi / (math.sin(math.pi * X) * gamma(1 - X, Y))
    else:
        Y = X
        while X < Y + 1:
            Y = Y + 1
            X = X * Y
        return gamma_coefficients(X, Y)

def gamma_coefficients(X, Y):
    # implementation of Taylor series approximation
    pass

def recip_gamma(X, Tolerance):
    # implementation using recursion and tolerance for early exit
    pass
```