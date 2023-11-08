```python
from itertools import count

def firstPrimeFactor(n):
    return next(i for i in range(2, n+1) if n % i == 0)

def allPrimeFactors(n):
    if n == 1:
        return []
    else:
        first = firstPrimeFactor(n)
        return [first] + allPrimeFactors(n // first)

def factorCount(n):
    if n == 1:
        return 1
    else:
        return 1 + len(list(group(allPrimeFactors(n))))

def divisorCount(n):
    return (n, factorCount(n))

def hcnNext(num, factors):
    for i in count(num):
        if factorCount(i) > factors:
            return (i, factorCount(i))

hcnSequence = [num for num, _ in (hcnNext(1, 1) for _ in range(20))]
print(hcnSequence)
```