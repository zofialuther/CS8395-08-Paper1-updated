```python
import random

def isPrime(n):
    return isMillerRabinPrime(100, n)

def isMillerRabinPrime(k, n):
    if n % 2 == 0:
        return n == 2
    elif n < 100:
        primes_to_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        return n in primes_to_100
    else:
        evens, odds = span(lambda x: x % 2 == 0, iterate(lambda x: x // 2, n - 1))
        ws = witnesses(k, n)
        return all(test(n, n - 1, evens, odds[0], a) for a in ws)

def test(n, n_1, evens, d, a):
    x = powerMod(n, a, d)
    powers = [powerMod(n, a, e) for e in evens]
    return x in [1, n_1] or n_1 in powers

def witnesses(k, n):
    if n < 9080191:
        return [31, 73]
    elif n < 4759123141:
        return [2, 7, 61]
    elif n < 3474749660383:
        return [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        return [2, 3, 5, 7, 11, 13, 17]
    else:
        g = random.SystemRandom()
        return [g.randint(2, n - 1) for _ in range(k)]

def powerMod(m, x, n):
    return f(n - 1, x, x) % m

def f(d, a, y):
    if d == 0:
        return y
    else:
        return g(d, a, y)

def g(i, b, y):
    if i % 2 == 0:
        return g(i // 2, (b * b) % m, y)
    else:
        return f(i - 1, b, (b * y) % m)
```