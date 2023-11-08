```python
from math import gcd
from itertools import permutations

def lcm(a, b):
    return a * b // gcd(a, b)

def mkint(radix, digits):
    val = 0
    for digit in digits:
        val = val * radix + digit
    return val

def combinations(radix, n_digits):
    domain = list(range(1, radix + 1))
    return permutations(domain, radix - n_digits)

def test(radix, digits, lcm_val):
    number = mkint(radix, digits)
    return number % lcm_val == 0

def bignum(radix):
    r0 = radix + 1
    for n in range(1, r0):
        n_digits = radix - n
        for trial in combinations(radix, n_digits):
            lcm_val = 1
            for digit in trial:
                lcm_val = lcm(lcm_val, digit)
            for perm in permutations(trial):
                if test(radix, perm, lcm_val):
                    return mkint(radix, perm)

def largest_decimal():
    return bignum(10)

def largest_hex():
    n = bignum(16)
    h = format(n, 'X')
    return n, h
```