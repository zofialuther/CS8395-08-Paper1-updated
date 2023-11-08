```python
import sympy

def successive_primes(offsets, max_prime):
    prev_prime = 2
    for offset in offsets:
        for prime in sympy.primerange(prev_prime, max_prime):
            if prime - prev_prime == offset:
                yield (prev_prime, prime)
                prev_prime = prime

for offset in [(2, 2), (2, 4), (4, 2)]:
    for prime in [20, 50, 100]:
        primes = list(successive_primes(offset, prime))
        print(f"Offset: {offset}, Max Prime: {prime}, Count: {len(primes)}")
        if primes:
            print(f"First Group: {primes[0]}, Last Group: {primes[-1]}")
        print()
```