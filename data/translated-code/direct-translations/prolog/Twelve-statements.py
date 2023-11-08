```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz("puzzle(L) :- L = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12], L ins 0..1, element(1, L, 1), A2 #<==> A7 + A8 + A9 + A10 + A11 + A12 #= 3, A3 #<==> A2 + A4 + A6 + A8 + A10 + A12 #= 2, A4 #<==> (A5 #==> (A6 #/\ A7)), A5 #<==> A2 + A3 + A4 #= 0, A6 #==> A1 + A3 + A5 + A7 + A9 + A11 #= 4, A7 #<==> A2 + A3 #= 1, A8 #<==> (A7 #==> A5 #/\ A6), A9 #<==> A1 + A2 + A3 + A4 + A5 + A6 #= 3, A10 #<==> A11 #/\ A12, A11 #<==> A7 + A8 + A9 #= 1, A12 #<==> A1 + A2 + A3 + A4 + A5 + A6 + A7 +A8 + A9 + A10 + A11 #= 4, label(L), numlist(1, 12, NL), write('Statements '), maplist(my_write, NL, L), writeln(' are true').")
prolog.assertz("my_write(N, 1) :- format('~w ', [N]).")
prolog.assertz("my_write(_N, 0).")

list(prolog.query("puzzle(L)"))
```