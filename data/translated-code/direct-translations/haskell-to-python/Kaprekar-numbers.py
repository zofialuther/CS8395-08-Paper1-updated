```python
from functools import reduce
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def unit_factors(n):
    factors = []
    for prime in primes():
        while n % prime == 0:
            factors.append(prime)
            n = n // prime
        if n == 1:
            return factors

def factors(n):
    unique_factors = set(unit_factors(n))
    all_factors = set()
    for factor in unique_factors:
        all_factors.add(factor)
        all_factors.add(n // factor)
    return sorted(all_factors)

def inverse(x, y):
    a, b = ext_euclid(x, y)
    if a < 0:
        a += y
    return a

def ext_euclid(x, y):
    if y == 0:
        return (1, 0)
    else:
        s, t = ext_euclid(y, x % y)
        q, r = divmod(x, y)
        return (t, s - q * t)

def kaprekar(base, top):
    kaps = set()
    for i in range(1, int(math.log(top * top // (base ** 2), base)) + 1):
        pb = base ** i - 1
        for x in factors(pb):
            if x == pb:
                kaps.add(pb)
            else:
                kaps.add(x * inverse(x, pb // x))
    return sorted(kaps)

def main():
    for kaprekar_number in kaprekar(10, 10000000):
        print(kaprekar_number)

main()
```