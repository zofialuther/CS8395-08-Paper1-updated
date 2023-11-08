```python
from itertools import takewhile
from functools import reduce
from math import isqrt

def isPrime(x):
    return all(x % i != 0 for i in takewhile(lambda p: p <= isqrt(x), primes))

def unitFactors(n):
    def f(n, ps):
        if n == 1:
            return []
        elif n == 0:
            return [n]
        else:
            for p in ps:
                if n % p == 0:
                    return [p] + f(n // p, [p] + ps)
            return f(n, ps)
            
    return map(lambda x: reduce(lambda a, b: a * b, x), group(f(n, list(takewhile(lambda p: p <= n, primes)))))

def factors(n):
    def f(x, a):
        return [x, x * a]
    
    return reduce(f, [1] + unitFactors(n))

def inverse(x, y):
    def extEuclid(x, y):
        if y == 0:
            return (1, 0)
        else:
            q, r = divmod(x, y)
            s, t = extEuclid(y, r)
            return (t, s - q * t)
    
    a, b = extEuclid(x, y)
    if a < 0:
        a = a + y
    return a

def kaprekars(base, top):
    pb = [base ** x - 1 for x in range(1, 100)]  # replace 100 with a suitable upper limit
    k = []
    for i in pb:
        if i <= top * top // (base ** 2):
            k.extend(kaps(i))
    return list(set(sorted(k)))

def main():
    for k in kaprekars(10, 10000000):
        print(k)
```