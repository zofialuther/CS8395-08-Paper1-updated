```python
from functools import partial

def fs(P, S, S1):
    for x in S:
        S1.append(P(x))

def f1(x):
    return x * 2

def f2(x):
    return x + 3

create_partial = partial

FSF1 = create_partial(fs, f1)
FSF2 = create_partial(fs, f2)

S = [1, 2, 3, 4, 5]
S1 = []
S2 = []

FSF1(S, S1)
FSF2(S, S2)

print(S1)
print(S2)
```