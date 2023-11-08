```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz("babbage_(B, B, Sq) :- B * B =:= Sq, number_chars(Sq, [_,2,_,6,_,9,_,6,_,9,_,6,_]).")
prolog.assertz("babbage_(B, R, Sq) :- N is B+1, babbage_(N, R, Sq).")
prolog.assertz("babbage(Num, Square) :- babbage_(1, Num, Square), format('lowest number is ~p which squared becomes ~p~n', [Num, Square]).")

list(prolog.query("babbage(Num, Square)"))
```