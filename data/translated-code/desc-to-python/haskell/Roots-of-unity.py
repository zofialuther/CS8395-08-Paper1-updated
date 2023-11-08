```python
import cmath

def rootsOfUnity(n):
    return [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]

result = rootsOfUnity(3)
print(result)
```