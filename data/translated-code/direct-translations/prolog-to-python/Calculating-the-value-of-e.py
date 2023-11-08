```python
from math import log

def newton(x0):
    return x0 * (2 - log(x0))

def e(iterations):
    eps = 1e-15
    x1, x2 = iterations[0], iterations[1]
    while abs(x2 - x1) >= eps:
        x1, x2 = x2, newton(x2)
    return x1

def main():
    iterations = [2]
    while True:
        next_value = newton(iterations[-1])
        iterations.append(next_value)
        if len(iterations) > 1 and abs(iterations[-1] - iterations[-2]) < 1e-15:
            break
    result = e(iterations)
    print(f"e = {result}")

if __name__ == "__main__":
    main()
```