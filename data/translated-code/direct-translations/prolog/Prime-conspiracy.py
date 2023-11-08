```python
import math

def nthprime(n, p):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime > math.isqrt(num):
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2
    return primes[-1] if n > 1 else 2

def conspiracy(m):
    n = 10**m
    p = nthprime(n)
    ps = sieve(p)
    counts = tally(ps)
    sorted_counts = sorted(counts.items())
    show(sorted_counts)

def show(results):
    for d1, d2, count in results:
        print(f"{d1} -> {d2}: {count}")

def tally(ps):
    counts = {}
    for i in range(len(ps)-1):
        d1, d2 = ps[i] % 10, ps[i+1] % 10
        key = (d1, d2)
        counts[key] = counts.get(key, 0) + 1
    return counts

def sieve(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*2, limit + 1, num):
                is_prime[multiple] = False
    return primes

# count results

conspiracy(5)
```