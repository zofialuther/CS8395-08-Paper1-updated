```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("lambda.pl")

# The Y combinator
def y(P, Arg, R):
    Pred = P + "\\Nb2^F2^call(P,Nb2,F2,P)"
    prolog.assertz(Pred)
    prolog.assertz("call(Pred, Arg, R)")

test_y_combinator = prolog.query("test_y_combinator")
for soln in test_y_combinator:
    print(soln)
```