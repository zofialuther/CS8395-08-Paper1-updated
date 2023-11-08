```python
def chinese_remainder_theorem(A, N):
    if len(A) != len(N):
        raise ValueError("A and N must have the same length")
    
    for n in N:
        if not is_prime(n):
            raise ValueError("All elements of N must be prime")

    product = 1
    for n in N:
        product *= n
    
    result = 0
    for ai, ni in zip(A, N):
        mi = product // ni
        result += ai * mi * mod_inverse(mi, ni)
    
    return result % product

def is_prime(n):
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
        i += 6
    return True

def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x
```