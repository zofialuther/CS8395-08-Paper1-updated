def isPrime(n):
    return not any((0 == (n % i)) for i in range(2, int(n**0.5) + 1))

primes = [i for i in range(2, 1000) if isPrime(i)]

def isKPrime(k, n):
    if k == 1:
        return isPrime(n)
    else:
        sprimes = [x for x in range(2, n) if n % x == 0]
        return any(isKPrime(k - 1, num) for num in sprimes)

def kPrimes(k):
    return [i for i in range(2, 1000) if isKPrime(k, i)]

if __name__ == "__main__":
    for k in range(1, 6):
        print("k = " + str(k) + ": " + " ".join(map(str, kPrimes(k)[:10])))