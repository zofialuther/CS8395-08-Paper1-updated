```python
def longPrimesUpTo(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def isLongPrime(num):
        return len(str(num)) >= 7

    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i] and isLongPrime(i)]

def display():
    for i in range(2, 64000, 1000):
        print(i, len(longPrimesUpTo(i)))

def main():
    long_primes = longPrimesUpTo(500)
    print(long_primes)
    print(len(long_primes))

if __name__ == "__main__":
    main()
```