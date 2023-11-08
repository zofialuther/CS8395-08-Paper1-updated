```python
import math

def nth_root(n, m):
    if n > 0:
        if n == 2:
            return math.sqrt(m)
        else:
            x = m / 2
            while True:
                y = (1 / n) * ((n - 1) * x + (m / (x ** (n - 1))))
                if abs(y - x) < 0.0001:
                    return y
                x = y
    elif n < 0:
        return 1 / nth_root(abs(n), m)
    else:
        return "Error: n cannot be 0"
```