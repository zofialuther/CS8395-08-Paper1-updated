```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("clpfd")

prolog.assertz("coins(Q, D, N, P, T) :- T #= 25*Q + 10*D + 5*N + P")
prolog.assertz("coins_for(T, Q, D, N, P) :- coins(Q, D, N, P, T), maplist(writeln, [Q, D, N, P])")

for soln in prolog.query("coins_for(100, Q, D, N, P)"):
    print(soln["Q"], soln["D"], soln["N"], soln["P"])
```