```python
# Python equivalent code

import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [i for i in range(start, end) if is_prime(i)]

def pairs_in_list(lst):
    return list(itertools.combinations(lst, 2))

def freq(pairs, pair):
    return pairs.count(pair)

def line(pair, count, total_pairs):
    frequency = count / total_pairs
    print(f"{pair}: {count} ({frequency:.2%})")

def groups(primes):
    return [primes[i:i+2] for i in range(len(primes) - 1)]

def main(start, end):
    primes = primes_in_range(start, end)
    prime_pairs = pairs_in_list(primes)
    prime_groups = groups(primes)
    total_pairs = len(prime_pairs)
    for group in prime_groups:
        count = freq(prime_pairs, group)
        line(group, count, total_pairs)

start = 1
end = 50
main(start, end)
```