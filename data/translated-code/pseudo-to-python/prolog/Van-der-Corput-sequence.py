```python
import random

def g(B, N, X):
    if N > 0:
        if N == 1:
            X = '0.' + str(random.randint(0, B))
        else:
            sequence = '0.'
            for i in range(N - 1):
                sequence += str(random.randint(0, B))
            X = sequence
```