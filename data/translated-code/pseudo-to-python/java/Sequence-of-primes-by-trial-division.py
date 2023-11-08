def getPrimes(start, end):
    primes = []
    for n in range(start, end+1):
        if isPrime(n):
            primes.append(n)
    return primes

def isPrime(x):
    if x < 3 or x % 2 == 0:
        return x == 2
    max = int(x ** 0.5) + 1
    for n in range(3, max, 2):
        if x % n == 0:
            return False
    return True

def main():
    primes = getPrimes(0, 100)
    for p in primes:
        print(p, end=" ")
        
main()