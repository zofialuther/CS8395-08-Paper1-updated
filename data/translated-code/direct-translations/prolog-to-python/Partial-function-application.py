def fs(P, S, S1):
    return list(map(P, S, S1))

def f1(X):
    return 2 * X

def f2(X):
    return X * X

def create_partial(P):
    return lambda S, S1: fs(P, S, S1)

def fs():
    FSF1 = create_partial(f1)
    FSF2 = create_partial(f2)

    S1 = [0, 1, 2, 3]
    S11 = FSF1(S1)
    print(f'{FSF1.__name__} : {S1} ==> {S11}')
    S12 = FSF2(S1)
    print(f'{FSF2.__name__} : {S1} ==> {S12}')

    S2 = [2, 4, 6, 8]
    S21 = FSF2(S2)
    print(f'{FSF2.__name__} : {S2} ==> {S21}')
    S22 = FSF1(S2)
    print(f'{FSF1.__name__} : {S2} ==> {S22}')

fs()