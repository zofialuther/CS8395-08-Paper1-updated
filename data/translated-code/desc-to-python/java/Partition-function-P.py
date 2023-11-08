```python
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def partitions(n):
    if n == 0:
        return 1
        
    total = 0
    k = 1
    sign = 1
    while True:
        pentagonal = k * (3 * k - 1) // 2
        if pentagonal > n:
            break
        total += sign * (partitions(n - pentagonal) + partitions(n - pentagonal - k))
        total %= 10**10
        k = -k if k > 0 else -k + 1
        sign = -sign
    return total

start_time = time.time()
result = partitions(6666)
elapsed_time = time.time() - start_time
print(f"Partition function for 6666: {result}")
print(f"Elapsed time: {elapsed_time} seconds")
```