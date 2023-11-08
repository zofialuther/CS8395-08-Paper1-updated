```python
import random

def isPrime(n):
    return isMillerRabinPrime(100, n)

def isMillerRabinPrime(k, n):
    if n % 2 == 0:
        return n == 2
    elif n < 100:
        return n in primesTo100
    else:
        evens, odds = span_even(iterate(div(n-1, 2)))
        ws = witnesses(k, n)
        return checkWitnesses(ws, n, n-1, evens, odds[0])

def checkWitnesses(ws, n, n_1, evens, d):
    for a in ws:
        x = powerMod(n, a, d)
        powers = list(map(lambda x: powerMod(n, a, x), evens))
        if x in [1, n_1] or n_1 in powers:
            return True
    return False

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
        g = random.Random()
        g.seed()
        return [g.randint(2, n-1) for _ in range(k)]

def powerMod(m, x, n):
    return f(n-1, x, x) % m
    where 
        f = lambda d, a, y: y if d == 0 else g(d, a, y)
        g = lambda i, b, y: g(i//2, b*b % m, y) if i % 2 == 0 else f(i-1, b, b*y % m)

primesTo100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```