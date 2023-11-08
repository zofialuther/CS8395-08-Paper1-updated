```python
from itertools import takewhile

def int2bin(x):
    result = []
    while x != 0:
        result.append(x % 2)
        x = x // 2
    return result

def trialfac(m):
    qs = [x for x in range(1, m//2+1) if (2*m*x + 1) % 8 in [1, 7] and isPrime(2*m*x + 1)]
    bs = int2bin(m)
    return next(x for x in qs if takewhile(lambda q: functools.reduce(lambda a, b: a % q * pm(b, q), bs, 1) != 1, qs))

def pm(n, b):
    return 2**b * n**2
```