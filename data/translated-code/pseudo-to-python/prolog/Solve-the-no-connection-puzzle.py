from prologpy import prolog

prolog("""
:- use_module(library(clpfd).

edge(a, b).
edge(b, c).
edge(c, d).
edge(d, e).

connected(A, B) :- edge(A, B); edge(B, A).

no_connection_puzzle(Vs) :-
    findall(Node, edge(Node, _); edge(_, Node), Lst),
    sort(Lst, SortedLst),
    length(SortedLst, Len),
    length(Vs, Len),
    Vs ins 1..Len,
    set_constraints(SortedLst, Vs),
    label(Vs).

set_constraints([], _).
set_constraints([H|T], Vs) :-
    set_constraint(H, T, Vs, VH, VT),
    set_constraints(VT, Vs).

set_constraint(_, [], _, [], []).
set_constraint(H, [H2|T], Vs, [VH|VT], NewT) :-
    (connected(H, H2) -> VH #\= V2; true),
    set_constraint(H, T, Vs, VT, NewT).
""")