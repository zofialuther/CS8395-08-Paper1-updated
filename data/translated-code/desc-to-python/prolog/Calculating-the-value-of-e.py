```python
import math

def newtons_method(tol):
    x0 = 1
    while True:
        x1 = x0 - (math.exp(x0) - 1) / math.exp(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

def main():
    tolerance = 0.0001
    e_approx = newtons_method(tolerance)
    print("Approximated value of e:", e_approx)

main()
```