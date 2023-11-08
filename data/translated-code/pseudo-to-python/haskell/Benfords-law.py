```python
import math
from functools import reduce

def fstdigit(n: int) -> int:
    return int(str(n)[0])

n = 1000
fibs = [1, 1] + [0] * (n - 2)

for i in range(2, n):
    fibs[i] = fibs[i - 1] + fibs[i - 2]

fibdata = list(map(fstdigit, fibs[:n]))

freqs = {}
for num in fibdata:
    if num in freqs:
        freqs[num] += 1
    else:
        freqs[num] = 1

tab = []
for i in range(1, 10):
    freq = freqs.get(i, 0)
    logval = math.log10(freq + 1)
    tab.append((i, freq, logval))

print(tab)
```