```python
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("next_sep(_, [], []).")
prolog.assertz("next_sep(SepList, [S | Rest], [S | Rest]) :- member(S, SepList).")
prolog.assertz("next_sep(SepList, [R | Rest], [R | Rest1]) :- next_sep(SepList, Rest, Rest1).")

prolog.assertz("my_sort(SepList, Sorted) :- msort(SepList, Sorted).")

prolog.assertz("multisplit(_, [], []).")
prolog.assertz("multisplit(SepList, [Token | Rest], Result) :- next_sep(SepList, Token, FirstPart), append(FirstPart, RestPart, Token), multisplit(SepList, RestPart, ResultRest), append(FirstPart, ResultRest, Result).")
```