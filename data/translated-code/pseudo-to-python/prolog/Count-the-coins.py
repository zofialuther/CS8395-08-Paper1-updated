from pyswip import Prolog, Functor, Variable
prolog = Prolog()

prolog.assertz(":- use_module(library(clpfd)).")

def coins(Q, D, N, P, T):
    Q in 0..T,
    D in 0..T,
    N in 0..T,
    P in 0..T,
    T #= Q*25 + D*10 + N*5 + P.

def coins_for(T):
    coins(Q, D, N, P, T),
    maplist(indomain, [Q, D, N, P]).
```