```python
import math

for i in range(1, 101):
    if math.isqrt(i)**2 == i:
        print(f"Door {i}: open")
    else:
        print(f"Door {i}: closed")
```