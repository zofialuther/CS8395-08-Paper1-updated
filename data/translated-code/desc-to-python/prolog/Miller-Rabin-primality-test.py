```python
import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    d, s = find_ds(n-1)
    for _ in range(k):
        x = random.randint(2, n-1)
        if not witness(x, s, d, n):
            return False
    return True

def find_ds(n):
    s = 0
    d = n
    while d % 2 == 0:
        d //= 2
        s += 1
    return d, s

def witness(a, s, d, n):
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(s-1):
        x = pow(x, 2, n)
        if x == n-1:
            return True
    return False
```