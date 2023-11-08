```python
class PrimeConspiracy:
    
    @staticmethod
    def main():
        limit = 1000000
        sieveLimit = 15500000

        buckets = [[0]*10 for _ in range(10)]
        prevDigit = 2
        notPrime = PrimeConspiracy.sieve(sieveLimit)

        n = 3
        primeCount = 1
        while primeCount < limit:
            if notPrime[n]:
                n += 1
                continue

            digit = n % 10
            buckets[prevDigit][digit] += 1
            prevDigit = digit
            primeCount += 1
            n += 1

        for i in range(10):
            for j in range(10):
                if buckets[i][j] != 0:
                    print(f"{i} -> {j} : {buckets[i][j] / (limit / 100.0)}")

    @staticmethod
    def sieve(limit):
        composite = [False] * limit
        composite[0] = composite[1] = True

        max = int(limit ** 0.5)
        for n in range(2, max + 1):
            if not composite[n]:
                for k in range(n * n, limit, n):
                    composite[k] = True
        return composite
```