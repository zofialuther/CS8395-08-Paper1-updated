```python
import math

def is_prime(n, precision=100):
    if n >= 341550071728321:
        return n.is_probable_prime(precision)

    int_n = int(n)
    if int_n in [1, 4, 6, 8]:
        return False
    if int_n in [2, 3, 5, 7]:
        return True

    primes_to_test = get_primes_to_test(n)
    if n == 3215031751:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for a in primes_to_test:
        if try_composite(a, d, n, s):
            return False
    return True

def is_prime_int(n):
    return is_prime(n, 100)

def is_prime_long(n):
    return is_prime(n, 100)

def get_primes_to_test(n):
    if n >= 3474749660383:
        return [2, 3, 5, 7, 11, 13, 17]
    if n >= 2152302898747:
        return [2, 3, 5, 7, 11, 13]
    if n >= 118670087467:
        return [2, 3, 5, 7, 11]
    if n >= 25326001:
        return [2, 3, 5, 7]
    if n >= 1373653:
        return [2, 3, 5]
    return [2, 3]

def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True
```