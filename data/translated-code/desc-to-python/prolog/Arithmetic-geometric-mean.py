```python
import math

def agm(A, G, Res):
    if abs(A - G) < 1.0e-15:
        Res = (A + G) / 2
    else:
        Res = agm((A + G) / 2, math.sqrt(A * G), Res)
    return Res
```