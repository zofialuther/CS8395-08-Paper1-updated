def create_partial(P, fs(P)):
    pass

def fs(P, S, S1):
    maplist(P, S, S1)

def f1(X, Y):
    Y = 2 * X

def f2(X, Y):
    Y = X * X

def fs():
    create_partial(f1, FSF1)
    create_partial(f2, FSF2)

    S1 = [0,1,2,3]
    call(FSF1,S1, S11)
    format('~w : ~w ==> ~w~n',[FSF1, S1, S11])
    call(FSF1,S1, S12)
    format('~w : ~w ==> ~w~n',[FSF2, S1, S12])

    S2 = [2,4,6,8]
    call(FSF1,S2, S21)
    format('~w : ~w ==> ~w~n',[FSF2, S2, S21])
    call(FSF2,S2, S22)
    format('~w : ~w ==> ~w~n',[FSF1, S2, S22])