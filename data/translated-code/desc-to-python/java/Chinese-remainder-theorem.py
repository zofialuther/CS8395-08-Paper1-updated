```python
def mulInv(a, m):
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

def chineseRemainder(n, a):
    prod = 1
    for i in n:
        prod *= i

    result = 0

    for i in range(len(n)):
        pp = prod // n[i]
        result += a[i] * mulInv(pp, n[i]) * pp

    return result % prod

# Sample input arrays
n = [3, 5, 7]
a = [2, 3, 2]

# Demonstrate usage of chineseRemainder method
print(chineseRemainder(n, a))  # Output: 23
```