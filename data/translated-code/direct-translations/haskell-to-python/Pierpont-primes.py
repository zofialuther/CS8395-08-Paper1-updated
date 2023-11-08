from math import isqrt
from sympy import primerange
from sympy import nextprime

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    x, *xs = a
    y, *ys = b
    if x < y:
        return [x] + merge(xs, b)
    return [y] + merge(a, ys)

def n_smooth(p):
    factors = list(primerange(1, p+1))
    primes = [nextprime(1)]
    for _ in range(isqrt(p)):
        primes.append(nextprime(primes[-1]))
    s = [1]
    for n in factors:
        s = merge(s, [n*x for x in s])
    return s

def pierpoints(kind):
    result = []
    for n in n_smooth(3):
        if kind == 'First':
            x = n+1
        else:
            x = n-1
        if isprime(x):
            result.append(x)
    return result

print("\nFirst 50 Pierpont primes of the first kind:\n")
for row in chunks(pierpoints('First'), 10):
    for prime in row:
        print(f"{comma_format(prime):>12}", end="")
    print("\n")
print("\nFirst 50 Pierpont primes of the second kind:\n")
for row in chunks(pierpoints('Second'), 10):
    for prime in row:
        print(f"{comma_format(prime):>12}", end="")
    print("\n")
print("\n250th Pierpont prime of the first kind:", comma_format(pierpoints('First')[249]))
print("\n250th Pierpont prime of the second kind:", comma_format(pierpoints('Second')[249]))