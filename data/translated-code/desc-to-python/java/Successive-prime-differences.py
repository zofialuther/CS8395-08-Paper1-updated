```python
def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

def find_successive_primes(primes, difference):
    result = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == difference:
            result.append((primes[i], primes[i + 1]))
    return result

def main():
    limit = 100
    primes = sieve_of_eratosthenes(limit)
    differences = [1, 2, 3, 5]
    for diff in differences:
        result = find_successive_primes(primes, diff)
        print(f"Successive prime numbers with difference {diff}: {result}")

if __name__ == "__main__":
    main()
```