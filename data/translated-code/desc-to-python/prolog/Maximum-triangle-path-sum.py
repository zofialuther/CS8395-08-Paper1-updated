```python
max_path(N, V) :-
    data(N, List),
    path(List, V, _).

data(1, [1]).
data(2, [3, 7, 4]).
data(3, [2, 4, 6, 8]).
data(4, [5, 9, 3, 7, 8]).

path([X], X, []).
path([A,B|T], V, [A|T1]) :-
    path([B|T], V1, T1),
    max(V, V1, V2),
    V is A+V2.

max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.
```