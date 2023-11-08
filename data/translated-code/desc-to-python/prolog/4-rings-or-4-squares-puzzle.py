```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("clpfd")

prolog.assertz("my_sum(Min, Max, Top, Lists, LL) :- length(L, 7), L ins Min..Max, (Top = 1 -> all_distinct(L) ; true), [A,B,C,D,E,F,G] = L, A + B + C + D + E + F + G #= Top, findall(L, labeling([], L), LL).")

prolog.assertz("my_sum_1(Min, Max, Top, Lists, LL) :- my_sum(Min, Max, Top, Lists, LL).")

prolog.assertz("my_sum_2(Min, Max, Top, Lists, LL) :- my_sum(Min, Max, Top, Lists, LL).")
```