```python
from itertools import combinations as cmb

def isP(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return n > 2 and all(n % x > 0 for x in range(3, int(n ** 0.5) + 1, 2))

def genP(n):
    p = [2]
    p.extend(x for x in range(3, n + 1) if isP(x) and x % 2 != 0)
    return p

data = [(10, 2), (20, 3)]

for tup in data:
    n, cnt = tup
    ci = cmb(genP(n), cnt)
    while True:
        try:
            c = next(ci)
            if sum(c) == n:
                print((n, cnt), c)
                break
        except StopIteration:
            print("Combination not possible")
            break
```