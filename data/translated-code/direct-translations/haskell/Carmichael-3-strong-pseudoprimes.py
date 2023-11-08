```python
from sympy import isprime

def carmichaels():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    result = []
    for p in primes:
        for h3 in range(2, p):
            g = h3 + p
            for d in range(1, g):
                if (g * (p - 1)) % d == 0 and (-1 * p * p) % h3 == d % h3:
                    q = 1 + (((p - 1) * g) // d
                    if isprime(q):
                        r = 1 + ((p * q) // h3)
                        if isprime(r) and (q * r) % (p - 1) == 1:
                            result.append((p, q, r))
    return result

print('\n'.join(map(str, carmichaels())))
```