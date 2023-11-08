```python
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes(limit):
    prime_list = []
    for num in range(2, limit + 1):
        if isPrime(num):
            prime_list.append(num)
    return prime_list

def isKPrime(n, k):
    prime_factors = []
    divisor = 2
    while n > 1 and len(prime_factors) <= k:
        if n % divisor == 0:
            prime_factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return len(prime_factors) == k

def kPrimes(k, limit):
    k_prime_list = []
    num = 2
    while len(k_prime_list) < limit:
        if isKPrime(num, k):
            k_prime_list.append(num)
        num += 1
    return k_prime_list

def main():
    for k in range(1, 6):
        print(f"The first 10 k-prime numbers for k = {k}: {kPrimes(k, 10)}")

if __name__ == "__main__":
    main()
```