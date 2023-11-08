```python
from itertools import takewhile, permutations, combinations
import sympy

def partitions(x, n):
    if n <= 1:
        if x in primes:
            return [x]
        else:
            return []
    else:
        ps = list(takewhile(lambda p: p <= x, primes))
        return go(ps, x, n)

def go(ps, x, n):
    if n == 1:
        if x in ps:
            return [x]
        else:
            return []
    else:
        result = []
        for p in ps:
            temp = go([i for i in ps if i != p and i <= x], x - p, n - 1)
            for t in temp:
                result.append([p] + t)
        return result

if __name__ == "__main__":
    primes = list(sympy.primerange(2, 1000))
    test_cases = [
        (99809, 1), 
        (18, 2), 
        (19, 3), 
        (20, 4), 
        (2017, 24), 
        (22699, 1),
        (22699, 2),
        (22699, 3)
    ]
    for x, n in test_cases:
        print(f"{(x, n)} -> {'+'.join(map(str, partitions(x, n))) if partitions(x, n) else '(no solution)'}")
```