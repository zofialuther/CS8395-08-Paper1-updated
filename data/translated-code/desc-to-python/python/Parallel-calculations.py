```python
import concurrent.futures
import math

def lowest_prime_factor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
    return num

def prime_factors(num):
    factors = []
    d = 2
    while d * d <= num:
        while (num % d) == 0:
            factors.append(d)
            num //= d
        d += 1
    if num > 1:
        factors.append(num)
    return factors

def main():
    numbers = [56, 34, 23, 78, 45, 89]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        lowest_prime_futures = {executor.submit(lowest_prime_factor, num): num for num in numbers}
        prime_factors_futures = {executor.submit(prime_factors, num): num for num in numbers}
        lowest_prime = max([(future.result(), num) for future, num in lowest_prime_futures.items()])
        prime_factors = [(future.result(), num) for future, num in prime_factors_futures.items() if num == lowest_prime[1]]
        print(f"The number with the largest minimum prime factor is {lowest_prime[1]} with prime factors {prime_factors[0][0]}")

if __name__ == "__main__":
    main()
```