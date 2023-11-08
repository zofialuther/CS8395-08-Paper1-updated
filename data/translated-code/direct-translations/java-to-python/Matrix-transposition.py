```python
import numpy as np

m = np.array([[1, 1, 1, 1],
              [2, 4, 8, 16],
              [3, 9, 27, 81],
              [4, 16, 64, 256],
              [5, 25, 125, 625]])

ans = np.zeros((m.shape[1], m.shape[0]))

for rows in range(m.shape[0]):
    for cols in range(m.shape[1]):
        ans[cols][rows] = m[rows][cols]

for i in ans:
    print(i)
```