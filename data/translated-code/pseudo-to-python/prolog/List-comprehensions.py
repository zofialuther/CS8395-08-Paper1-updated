```python
from itertools import product

def my_bind(V, Xs):
    for i in Xs:
        V = i
        yield V

def interval(M, N):
    return range(M, N+1)

def list_comprehension(Var, Dec, Pred=None):
    if Pred:
        return [Var for Var in product(*Dec) if Pred(*Var)]
    else:
        return [Var for Var in product(*Dec)]
```