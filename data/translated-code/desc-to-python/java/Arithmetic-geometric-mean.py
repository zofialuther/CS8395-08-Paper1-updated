```python
import math

a = 1
b = 1 / math.sqrt(2)
threshold = 0.0001

while abs(a - b) > threshold:
    a = (a + b) / 2
    b = math.sqrt(a * b)

print("Arithmetic-Geometric Mean:", (a + b) / 2)
```