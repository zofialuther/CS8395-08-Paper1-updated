```python
import random

def is_Prime(n):
    if not isinstance(n, int):
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d = d >> 1
        s = s + 1
    assert(2**s * d == n - 1)
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, (2**i * d), n) == n - 1:
                return False
        return True
    for i in range(1, 8):
        a = random.randint(2, n)
        if trial_composite(a):
            return False
    return True

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def rotations(n):
    a = str(n)
    return {int(a[i:] + a[:i]) for i in range(len(a))}

def isCircular(n):
    return all(isPrime(int(o)) for o in rotations(n))

def main():
    result = [2, 3, 5, 7]
    first = '137'
    latter = '1379'
    for i in range(1, 6):
        s = {int(''.join(a)) for a in product(first, *((latter,) * i))}
        while s:
            a = s.pop()
            b = rotations(a)
            if isCircular(a):
                result.append(min(b))
            s -= b
    result.sort()
    return result

assert [2, 3, 5, 7, 11, 13, 17, 37, 79, 113, 197, 199, 337, 1193, 3779, 11939, 19937, 193939, 199933] == main()

repunit = lambda n: int('1' * n)

def repmain(n):
    result = []
    i = 2
    while len(result) < n:
        if is_Prime(repunit(i)):
            result.append(i)
        i = i + 1
    return result

assert [2, 19, 23, 317, 1031] == repmain(5)
```