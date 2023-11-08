```python
class LongPrimes:
    @staticmethod
    def sieve(limit, primes):
        c = [False] * limit
        p = 3
        p2 = p * p
        while p2 <= limit:
            for i in range(p2, limit, 2 * p):
                c[i] = True
            while c[p]:
                p += 2
            p2 = p * p
        for i in range(3, limit, 2):
            if not c[i]:
                primes.append(i)

    @staticmethod
    def find_period(n):
        r = 1
        period = 0
        for i in range(1, n):
            r = (10 * r) % n
        rr = r
        while r != rr:
            r = (10 * r) % n
            period += 1
        return period

    @staticmethod
    def main():
        numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]
        totals = [0] * len(numbers)
        primes = []
        long_primes = []
        LongPrimes.sieve(64000, primes)
        for prime in primes:
            if LongPrimes.find_period(prime) == prime - 1:
                long_primes.append(prime)
        count = 0
        index = 0
        for long_prime in long_primes:
            if long_prime > numbers[index]:
                totals[index] = count
                index += 1
            count += 1
        totals[-1] = count
        print("The long primes up to", numbers[0], "are:")
        print(long_primes[:totals[0]])
        print()
        print("The number of long primes up to:")
        for i in range(8):
            print(f"{numbers[i]:>5} is {totals[i]}")

LongPrimes.main()
```