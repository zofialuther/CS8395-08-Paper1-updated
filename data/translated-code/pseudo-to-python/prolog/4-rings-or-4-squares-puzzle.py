from pyswip import Prolog

prolog = Prolog()
prolog.assertz("use_module(library(clpfd))")

def my_sum(Min, Max, Top, LL):
    L = ['A','B','C','D','E','F','G']
    prolog.assertz("L ins " + str(Min) + ".." + str(Max))
    if Top == 0:
        prolog.assertz("all_distinct(L)")
    prolog.assertz("R #= A+B, R #= B+C+D, R #= D+E+F, R #= F+G, setof(L, labeling([ff], L), LL)")

def my_sum_1(Min, Max):
    prolog.assertz("my_sum(" + str(Min) + "," + str(Max) + ",0,LL), maplist(writeln, LL)")

def my_sum_2(Min, Max, Len):
    prolog.assertz("my_sum(" + str(Min) + "," + str(Max) + ",1,LL), length(LL," + str(Len) + ")")