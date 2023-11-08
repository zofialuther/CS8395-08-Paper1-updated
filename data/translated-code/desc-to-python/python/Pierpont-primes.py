```python
import random

def is_Prime(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for i in range(k):
        x = pow(random.randint(2, n - 1), d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True

def Pierpont_Primes(kind, n):
    primes = []
    num = 0
    while len(primes) < n:
        num += 1
        if kind == 1:
            if is_Prime(num) and is_Prime(2**num+1):
                primes.append(num)
        elif kind == 2:
            if is_Prime(num) and is_Prime(3**num+1):
                primes.append(num)
    return primes

def main():
    print("First 50 Pierpont primes of the first kind:", Pierpont_Primes(1, 50))
    print("First 50 Pierpont primes of the second kind:", Pierpont_Primes(2, 50))
    print("250th Pierpont prime of the first kind:", Pierpont_Primes(1, 250)[-1])
    print("250th Pierpont prime of the second kind:", Pierpont_Primes(2, 250)[-1])

if __name__ == "__main__":
    main()
```