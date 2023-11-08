```python
class Test:
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def getPrimes(self, start, end):
        return (x for x in range(start, end) if self.isPrime(x))

    def main(self):
        primes = self.getPrimes(0, 100)
        for prime in primes:
            print(prime)
```