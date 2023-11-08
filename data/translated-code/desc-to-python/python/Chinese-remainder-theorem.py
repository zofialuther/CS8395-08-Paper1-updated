```python
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = 1
    for i in n:
        prod *= i
    for i in range(len(n)):
        p = prod // n[i]
        sum += a[i] * mul_inv(p, n[i]) * p
    return sum % prod

n = [5, 7, 11]
a = [2, 3, 6]
print(chinese_remainder(n, a))  # Output: 17
```