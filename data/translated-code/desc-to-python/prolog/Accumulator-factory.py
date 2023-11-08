from pyswip import Prolog

prolog = Prolog()
prolog.assertz("define_g(N, V) :- asserta(user:V=N), G = \\(X, Y) -> user:V=N1, Y is X + N1, retract(user:V), asserta(user:V=Y).")
prolog.assertz("accumulator(X, Result) :- define_g(1, V), G = user:V, call(G, 5, Result1), write(Result1), nl, call(G, 2.3, Result2), write(Result2).")

list(prolog.query("accumulator(X, Result)"))