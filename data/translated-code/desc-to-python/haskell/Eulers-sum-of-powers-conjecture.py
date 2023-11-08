```python
import math

tuples = []
for x0 in range(251, 1000):
    for x1 in range(251, x0):
        for x2 in range(251, x1):
            for x3 in range(251, x2):
                if x0 > x1 > x2 > x3:
                    sum_of_powers = x0**5 + x1**5 + x2**5 + x3**5
                    root = round(sum_of_powers**(1/5))
                    if root**5 == sum_of_powers:
                        tuples.append((x0, x1, x2, x3, root))

print(tuples[0])
```