```python
class Isprime:
    def __init__(self, maximum):
        self.maximum = maximum
        self.primes = self._sieve(maximum)

    def _sieve(self, n):
        sieve = [True] * (n+1)
        sieve[0:2] = [False, False]
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [x for x in range(n+1) if sieve[x]]

    def carmichael(self, n):
        carmichaels = []
        for x in range(2, n+1):
            if x not in self.primes:
                for i in range(2, x):
                    if pow(i, x, x) != i:
                        break
                else:
                    carmichaels.append(x)
        return carmichaels

isprime = Isprime(2)
for i in range(1, 63):
    carmichaels = isprime.carmichael(i)
    print(f"Carmichael numbers for {i}: {carmichaels}")
```