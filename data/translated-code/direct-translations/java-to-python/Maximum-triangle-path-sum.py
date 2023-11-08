```python
import numpy as np

data = np.loadtxt("triangle.txt", dtype=int)

for r in range(len(data) - 1, 0, -1):
    for c in range(len(data[r]) - 1):
        data[r-1][c] += max(data[r][c], data[r][c+1])

print(data[0][0])
```