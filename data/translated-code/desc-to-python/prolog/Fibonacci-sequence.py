from pyswip import Prolog

prolog = Prolog()

prolog.assertz("fib(0, 0).")
prolog.assertz("fib(1, 1).")
prolog.assertz("fib(N, F) :- N > 1, N1 is N - 1, N2 is N - 2, fib(N1, F1), fib(N2, F2), F is F1 + F2.")

list(prolog.query("fib(N, X), N =< 15"))