```python
def sieve(N):
    primes = [2]
    composite = set()

    def sieve_once(p, n):
        for i in range(p, n+1, p):
            if i not in composite:
                composite.add(i)

    def sieve_recurse(p, n):
        for i in range(p, n+1):
            if i not in composite:
                primes.append(i)
                sieve_once(i, n)

    sieve_recurse(2, N)
    return primes
```