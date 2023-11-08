from pyswip import Prolog, Functor, Variable

prolog = Prolog()

prolog.assertz("cont_fact(0, F, Pred) :- call(Pred, 1, F).")
prolog.assertz("cont_fact(N, F, Pred) :- N > 0, N1 is N - 1, P = Z-T-(T is Z * N), cont_fact(N1, FT, P), call(Pred, FT, F).")

prolog.assertz("fact(N, FN) :- cont_fact(N, FN, \\X^Y^(Y = X)).")

for soln in prolog.query("fact(5, X)"):
    print(soln["X"])