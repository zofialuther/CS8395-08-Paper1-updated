def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def primes():
    primeList = []
    for i in range(2, 100):
        if isPrime(i):
            primeList.append(i)
    return primeList

def isKPrime(k, n):
    if k == 1:
        return isPrime(n)
    else:
        sprimes = []
        for p in primes():
            if n % p == 0:
                sprimes.append(p)
        for sp in sprimes:
            if isKPrime(k - 1, n // sp):
                return True
        return False

def kPrimes(k):
    kPrimeList = []
    for i in range(2, 100):
        if isKPrime(k, i):
            kPrimeList.append(i)
    return kPrimeList

def main():
    for k in range(1, 6):
        kPrimeList = kPrimes(k)
        print("k = " + str(k) + ": " + str(kPrimeList[:10]))