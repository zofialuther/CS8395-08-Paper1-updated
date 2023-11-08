```python
from functools import lru_cache
import math

@lru_cache(maxsize=None)
def lah_number(n, k):
    if n == 0 or k == 0:
        return 0
    if n == 1 and k == 1:
        return 1
    if k > n:
        return 0
    return (n-1+k)*lah_number(n-1, k) + lah_number(n-1, k-1)

def print_lah_numbers_up_to_n(n):
    for i in range(1, n+1):
        print(f"L({n}, {i}) = {lah_number(n, i)}")

def max_lah_number(n):
    max_val = 0
    for i in range(1, n+1):
        max_val = max(max_val, lah_number(n, i))
    return max_val

n = 12
print_lah_numbers_up_to_n(n)
print(f"Maximum value of L(100, k) is: {max_lah_number(100)}")
```