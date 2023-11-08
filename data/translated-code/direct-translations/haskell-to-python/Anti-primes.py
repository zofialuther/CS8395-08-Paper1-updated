```python
from itertools import count

def first_prime_factor(n):
    return next(x for x in range(2, n + 1) if n % x == 0)

def all_prime_factors(n):
    if n == 1:
        return []
    first = first_prime_factor(n)
    return [first] + all_prime_factors(n // first)

def factor_count(n):
    if n == 1:
        return 1
    return 1
    result = 1
    for _, group in groupby(all_prime_factors(n)):
        result *= len(list(group)) + 1
    return result

def divisor_count(n):
    return factor_count(n), 

def hcn_next(num, factors):
    for i in count(num):
        if factor_count(i) > factors:
            return i, factor_count(i)

def hcn_sequence():
    num, factors = 1, 1
    while True:
        yield num
        num, factors = hcn_next(num, factors)

if __name__ == "__main__":
    print(list(itertools.islice(hcn_sequence(), 20)))
```