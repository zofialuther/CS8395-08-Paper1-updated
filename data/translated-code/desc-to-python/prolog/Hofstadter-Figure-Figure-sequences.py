```python
from constraint_handling_rules import *

@chr_constraint
def ffr(x, R):
    if (x > 0) and (x not in R):
        R.add(x)

@chr_constraint
def ffs(x, S):
    if (x > 0) and (x not in S):
        S.add(x)

@chr_rule
def compute_ffr(x, R, S):
    if x > 0:
        ffr(x, R) <= ffs(x-1, S)

@chr_rule
def compute_ffs(x, S, R):
    if x > 0:
        ffs(x, S) <= ffr(x-1, R)

R = set()
S = set()
ffr(1, R)
ffs(2, S)

N = 10
for i in range(3, N+1):
    compute_ffr(i, R, S)
    compute_ffs(i, S, R)

```