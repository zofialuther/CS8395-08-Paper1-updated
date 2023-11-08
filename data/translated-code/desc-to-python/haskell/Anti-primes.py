```python
import math

def first_prime_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

def factor_count(n):
    factors = prime_factors(n)
    factor_count = 1
    current_factor = factors[0]
    current_count = 1
    for i in range(1, len(factors)):
        if factors[i] == current_factor:
            current_count += 1
        else:
            factor_count *= (current_count + 1)
            current_factor = factors[i]
            current_count = 1
    factor_count *= (current_count + 1)
    return factor_count

def divisor_count(n):
    return factor_count(n)

def next_hcn(current_hcn):
    n = current_hcn + 1
    while True:
        if factor_count(n) > factor_count(current_hcn):
            return n
        n += 1

def hcn_sequence(length):
    sequence = [1]
    current_hcn = 1
    for _ in range(length - 1):
        current_hcn = next_hcn(current_hcn)
        sequence.append(current_hcn)
    return sequence

def main():
    hcn_seq = hcn_sequence(20)
    print(hcn_seq)

if __name__ == "__main__":
    main()
```