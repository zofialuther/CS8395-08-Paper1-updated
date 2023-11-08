```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz("dot(V1, V2, N) :- maplist(product, V1, V2, P), sumlist(P, N).")
prolog.assertz("product(N1, N2, N3) :- N3 is N1 * N2.")
prolog.assertz("mmult(M1, M2, M3) :- transpose(M2, MT), maplist(mult_helper(MT), M1, M3).")
prolog.assertz("mult_helper(M2, I1, M3) :- maplist(dot(I1), M2, M3).")
```