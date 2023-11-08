from pyswip import Functor, Variable, Query, call, Prolog

prolog = Prolog()

def knapsack(L, N, R, LW, LV, WM, VM):
    length(L, N)
    length(R, N)
    R.unify(0, 1)
    maplist(arg(2), L, LW)
    maplist(arg(3), L, LV)
    scalar_product(LW, R, '#=<', 400)
    scalar_product(LV, R, '#=', VM)
    labeling([max(VM)], R)
    scalar_product(LW, R, '#=', WM)
    compute_lenword(L, 0, Len)
    print_results(A1,A2,A3, L, R, WM, VM)

def compute_lenword(L, N, NF):
    if L == []:
        NF.unify(N)
    else:
        item = L[0]
        Name, _, _ = item
        atom_length(Name, L)
        if L > N:
            N1 = L
        else:
            N1 = N
        compute_lenword(L[1:], N1, NF)

def print_results(A1, A2, A3, L, R, WM, VM):
    if L == []:
        sformat(W1, A1, [' '])
        sformat(W2, A2, [WM])
        sformat(W3, A3, [VM])
        format('~w~w~w~n', [W1,W2,W3])
    else:
        item = L[0]
        _, W, V = item
        if R[0] == 0:
            print_results(A1,A2,A3, L[1:], R[1:], WM, VM)
        else:
            sformat(W1, A1, [Name])
            sformat(W2, A2, [W])
            sformat(W3, A3, [V])
            format('~w~w~w~n', [W1,W2,W3])
            print_results(A1, A2, A3, L[1:], R[1:], WM, VM)