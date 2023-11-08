```python
def primes(limit):
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return [num for num in range(2, limit + 1) if sieve[num]]

def truncatableprime(num, primes_set):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if int(num_str[i:]) not in primes_set or int(num_str[:i]) not in primes_set:
            return False
    return True

limit = 1000000
prime_list = primes(limit)
primes_set = set(prime_list)

longest_truncatable_prime = 0
for prime in prime_list:
    if prime < 10:
        continue
    if truncatableprime(prime, primes_set):
        longest_truncatable_prime = prime

print(longest_truncatable_prime)
```
