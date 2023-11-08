```python
def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

def find_sexy_primes(primes):
    sexy_groups = []
    unsexy_primes = []
    for i in range(len(primes)-1):
        if primes[i+1] - primes[i] == 6:
            sexy_groups.append((primes[i], primes[i+1]))
        else:
            unsexy_primes.append(primes[i])
    last_10_unsexy = unsexy_primes[-10:]
    return sexy_groups, last_10_unsexy

limit = 1000
primes = sieve_of_eratosthenes(limit)
sexy_groups, last_10_unsexy = find_sexy_primes(primes)
print("Sexy prime groupings:", sexy_groups)
print("Last 10 unsexy prime numbers:", last_10_unsexy)
```