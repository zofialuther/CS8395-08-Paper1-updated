```python
def sieve(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

def findPeriod(num):
    if num == 1:
        return 0
    remainder = 10 % num
    period = 1
    while remainder != 1:
        remainder = (remainder * 10) % num
        period += 1
    return period

primes_list = sieve(64000)

long_primes_up_to_500 = [prime for prime in primes_list if findPeriod(prime) == prime - 1]

specific_numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]

long_primes_counts = [len([prime for prime in primes_list if findPeriod(prime) == prime - 1 and prime <= num]) for num in specific_numbers]

print("Long primes up to 500:", long_primes_up_to_500)
print("Number of long primes up to each specified number:", long_primes_counts)
```