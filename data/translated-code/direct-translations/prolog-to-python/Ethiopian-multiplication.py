from pyswip import Prolog

prolog = Prolog()

prolog.assertz("mul(1, Y, S) :- S = Y.")
prolog.assertz("mul(X, Y, S) :- X \\= 1, X1 is X // 2, Y1 is Y * 2, mul(X1, Y1, S1), add_if_odd(X, Y, S1, S).")
prolog.assertz("even(X) :- 0 is X mod 2, !.")
prolog.assertz("even(X) :- 1 is X mod 2, !.")
prolog.assertz("add_if_odd(X, _, A, S) :- even(X), !, S is A.")
prolog.assertz("add_if_odd(X, Y, A, S) :- \\+ even(X), !, S is A + Y.")

Z = list(prolog.query("mul(17, 34, Z), writeln(Z)"))[0]["Z"]
print(Z)