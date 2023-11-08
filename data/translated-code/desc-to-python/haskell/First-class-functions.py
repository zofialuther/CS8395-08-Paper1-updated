```python
import math

def cube(x):
    return x ** 3

def croot(x):
    return x ** (1/3)

funclist = [math.sin, math.cos, math.tan]
invlist = [math.asin, math.acos, math.atan]

def main():
    result = list(map(lambda f, g: f(g(0.5)), funclist, invlist))
    print(result)

main()
```