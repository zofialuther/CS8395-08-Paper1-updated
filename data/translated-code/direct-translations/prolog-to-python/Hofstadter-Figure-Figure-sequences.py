```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("library(chr)")

prolog.assertz(":- chr_constraint ffr/2, ffs/2, hofstadter/1,hofstadter/2.")
prolog.assertz(":- chr_option(debug, off).")
prolog.assertz(":- chr_option(optimize, full).")

prolog.assertz("ffr(N, R1) \ ffr(N, R2) <=> R1 = R2 | True.")
prolog.assertz("ffs(N, R1) \ ffs(N, R2) <=> R1 = R2 | True.")

prolog.assertz("""
    ffr(N, R), ffr(N1, R1), ffs(N1,S1) ==>
         N > 1, N1 is N - 1 |
	     R is R1 + S1.
""")

prolog.assertz("""
    ffs(N, S), ffs(N1,S1) ==>
         N > 1, N1 is N - 1 |
	     V is S1 + 1,
	     (   find_chr_constraint(ffr(_, V)) ->  S is V+1; S = V).
""")

prolog.assertz("hofstadter(N) ==>  ffr(1,1), ffs(1,2).")

prolog.assertz("hofstadter(N), ffr(N1, _R), ffs(N1, _S) ==> N1 < N, N2 is N1 +1 |  ffr(N2,_), ffs(N2,_).")
```