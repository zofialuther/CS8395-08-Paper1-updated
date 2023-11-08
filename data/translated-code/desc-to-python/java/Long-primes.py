class LongPrimes:
    def __init__(self):
        pass
    
    def sieve(self, n):
        primes = []
        is_prime = [True] * (n+1)
        for p in range(2, n+1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p*p, n+1, p):
                    is_prime[i] = False
        return primes
    
    def reciprocal_period(self, n):
        if n % 2 == 0 or n % 5 == 0:
            return 0
        period = 1
        while (10 ** period - 1) % n != 0:
            period += 1
        return period
    
    def find_long_primes(self, limit):
        primes = self.sieve(limit)
        long_primes = []
        for prime in primes:
            if self.reciprocal_period(prime) == prime - 1:
                long_primes.append(prime)
        return long_primes

if __name__ == "__main__":
    lp = LongPrimes()
    long_primes_up_to_64000 = lp.find_long_primes(64000)
    print("Long primes up to 64000:", long_primes_up_to_64000)
    print("Total count of long primes up to 64000:", len(long_primes_up_to_64000))