```python
import math

def compose(f, g):
    return lambda x: f(g(x))

def zipWith(f, xs, ys):
    return [f(x, y) for x, y in zip(xs, ys)]

def main():
    functions = [
        compose(math.sin, math.cos),
        compose(math.asin, math.acos),
        lambda x: x**3,
        lambda x: x**(1/3)
    ]
    result = [f(0.5) for f in functions]
    print(result)

main()
```