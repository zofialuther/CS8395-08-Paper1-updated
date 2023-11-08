```python
from itertools import product

def g(B, N):
    if N == 0:
        return ['0.0']
    else:
        sequences = [''.join(str(i) for i in seq) for seq in product(range(B+1), repeat=N)]
        return sequences

B = 3
N = 2
result = g(B, N)
print(result)
```
Output:
['00', '01', '02', '03', '10', '11', '12', '13', '20', '21', '22', '23', '30', '31', '32', '33']