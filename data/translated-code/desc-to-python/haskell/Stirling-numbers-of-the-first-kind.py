```python
from functools import lru_cache

@lru_cache(maxsize=None)
def stirling1(n, k):
    if n == 0 and k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    else:
        return (n-1)*stirling1(n-1, k) + stirling1(n-1, k-1)

table = [[stirling1(n, k) for k in range(1, 101)] for n in range(1, 101)]

for row in table:
    print(" ".join(str(num).rjust(10) for num in row))

max_val = max(stirling1(100, k) for k in range(1, 101))
print("Maximum value of S1(100, k) for k ranging from 1 to 100:", max_val)
```