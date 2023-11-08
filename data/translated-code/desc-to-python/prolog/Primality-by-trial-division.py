```python
import math

def prime(N):
    if N < 2:
        return False
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return False
    return True
```