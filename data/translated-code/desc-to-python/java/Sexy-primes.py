```python
class SexyPrimes:
    def __init__(self, max_value):
        self.max_value = max_value
        self.primes = self.sieve_of_eratosthenes(max_value)
        self.sexy_primes = 0
        self.sexy_triples = 0
        self.sexy_quadruplets = 0
        self.unsexy_primes = 0

    def sieve_of_eratosthenes(self, n):
        primes = [True] * (n+1)
        primes[0], primes[1] = False, False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        return [i for i in range(len(primes)) if primes[i]]

    def is_sexy_prime(self, a, b):
        return abs(a - b) == 6

    def is_sexy_triple(self, a, b, c):
        return self.is_sexy_prime(a, b) and self.is_sexy_prime(b, c)

    def is_sexy_quadruplet(self, a, b, c, d):
        return self.is_sexy_triple(a, b, c) and self.is_sexy_prime(c, d)

    def count_sexy_primes(self):
        for i in range(len(self.primes) - 1):
            if self.is_sexy_prime(self.primes[i], self.primes[i+1]):
                self.sexy_primes += 1

    def count_sexy_triples(self):
        for i in range(len(self.primes) - 2):
            if self.is_sexy_triple(self.primes[i], self.primes[i+1], self.primes[i+2]):
                self.sexy_triples += 1

    def count_sexy_quadruplets(self):
        for i in range(len(self.primes) - 3):
            if self.is_sexy_quadruplet(self.primes[i], self.primes[i+1], self.primes[i+2], self.primes[i+3]):
                self.sexy_quadruplets += 1

    def count_unsexy_primes(self):
        self.unsexy_primes = len(self.primes) - 1 - (self.sexy_primes + self.sexy_triples + self.sexy_quadruplets)

    def display_results(self):
        print(f"Sexy Primes: {self.sexy_primes}")
        print(f"Sexy Triples: {self.sexy_triples}")
        print(f"Sexy Quadruplets: {self.sexy_quadruplets}")
        print(f"Unsexy Primes: {self.unsexy_primes}")
        print(f"Prime Numbers: {self.primes}")

    def main(self):
        self.count_sexy_primes()
        self.count_sexy_triples()
        self.count_sexy_quadruplets()
        self.count_unsexy_primes()
        self.display_results()

max_value = 100
sp = SexyPrimes(max_value)
sp.main()
```