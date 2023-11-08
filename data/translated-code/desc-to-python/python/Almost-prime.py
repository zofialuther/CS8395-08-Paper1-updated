```python
def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors

def k_almost_prime(start, end, k):
    almost_prime_numbers = []
    for num in range(start, end+1):
        if len(prime_factors(num)) == k:
            almost_prime_numbers.append(num)
    print(f"{k}-almost-prime numbers between {start} and {end}: {almost_prime_numbers}")

k_almost_prime(1, 100, 2)
k_almost_prime(1, 100, 3)
k_almost_prime(1, 100, 4)
```