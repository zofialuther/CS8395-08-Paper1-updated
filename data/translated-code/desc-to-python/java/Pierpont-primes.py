```python
from math import pow

def pierpont_primes():
    primes = []
    n = 1
    while len(primes) < 50:
        p = 2**n + 1
        if is_prime(p):
            primes.append(p)
        n += 1
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
    return True

pierpont_primes_list = pierpont_primes()
print(pierpont_primes_list)

def nth_pierpont_prime(n):
    count = 0
    num = 1
    while count < n:
        if is_pierpont_prime(num):
            count += 1
        num += 1
    return num - 1

def is_pierpont_prime(num):
    return is_prime(num) and (num - 1) % 2 == 0

print(nth_pierpont_prime(250))
```