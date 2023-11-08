from pyswip import Prolog

prolog = Prolog()
prolog.assertz("plus(X, Y, Z) :- Z is X + Y.")

result = list(prolog.query("plus(4, 5, Result)"))
print(result)