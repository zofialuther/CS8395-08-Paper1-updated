```python
import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
        if n % d == 0:
            return False
        d += 4
    return True

def findCombo(k, x, m, n, combo):
    foundCombo = False
    if k >= m:
        if sum([primes[combo[i]] for i in range(m)]) == x:
            print(f"The partitioned number is {x} and the prime numbers are {[primes[combo[i]] for i in range(m)]}")
            foundCombo = True
    else:
        for j in range(n):
            if k == 0 or j > combo[k-1]:
                combo[k] = j
                if not foundCombo:
                    foundCombo = findCombo(k+1, x, m, n, combo)
    return foundCombo

def partition(x, m):
    if x < 2 or m < 1 or m >= x:
        raise ValueError("Invalid input")
    filteredPrimes = [i for i in range(2, x+1) if isPrime(i)]
    n = len(filteredPrimes)
    if n < m:
        raise ValueError("Not enough primes")
    combo = [0] * m
    foundCombo = findCombo(0, x, m, n, combo)
    if not foundCombo:
        print("It is not possible to partition the number")

primes = [i for i in range(2, 30) if isPrime(i)]
partition(20, 3)
```