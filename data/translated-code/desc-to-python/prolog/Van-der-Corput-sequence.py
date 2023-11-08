```python
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("g(0, _, []).")
prolog.assertz("g(N, B, [X|Xs]) :- N > 0, between(0, B, X), N1 is N-1, g(N1, B, Xs).")
```