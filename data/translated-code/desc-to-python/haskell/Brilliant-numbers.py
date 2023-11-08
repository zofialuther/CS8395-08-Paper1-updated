```python
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n+1):
        if is_prime(i):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n == 1:
            break
    return factors

def isBrilliant(num):
    factors = prime_factors(num)
    unique_factors = list(set(factors))
    count = [factors.count(factor) for factor in unique_factors]
    return len(set(count)) == 1

def table(data):
    col_width = max(len(str(word)) for row in data for word in row) + 2
    for row in data:
        print("".join(str(word).ljust(col_width) for word in row))

def main():
    brilliant_numbers = [num for num in range(2, 101) if isBrilliant(num)]
    data = [["Brilliant Numbers"]]
    data.extend([[num] for num in brilliant_numbers])
    table(data)

if __name__ == "__main__":
    main()
```