```python
import math

def isqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number is undefined")
    if x < 2:
        return x
    low = 0
    high = x
    while low + 1 < high:
        mid = (low + high) // 2
        if mid * mid <= x:
            low = mid
        else:
            high = mid
    return low

# Print integer square roots for a range of numbers
for num in range(1, 11):
    print(f"Integer square root of {num} is {isqrt(num)}")

# Print integer square roots of powers of 7
for power in range(1, 6):
    num = 7 ** power
    root = isqrt(num)
    print(f"Integer square root of 7^{power} is {root}")
```