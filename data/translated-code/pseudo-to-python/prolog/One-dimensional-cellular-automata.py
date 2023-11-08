def one_dimensional_cellular_automata(L):
    for i in L:
        print(i, end='')
    print('\n')
    N = len(L)
    LN = [0] * N
    compute_next([0] + L, LN)
    if L != LN:
        one_dimensional_cellular_automata(LN)
    else:
        return True

def compute_next(L, R1):
    if L[:3] == [0, 0, 0]:
        compute_next([0, 0] + L[3:], R1)
    elif L[:3] == [0, 0, 1]:
        compute_next([0, 1] + L[3:], R1)
    elif L[:3] == [0, 1, 0]:
        compute_next([1, 0] + L[3:], R1)
    elif L[:3] == [0, 1, 1]:
        compute_next([1, 1] + L[3:], R1)
    elif L[:3] == [1, 0, 0]:
        compute_next([0, 0] + L[3:], R1)
    elif L[:3] == [1, 0, 1]:
        compute_next([0, 1] + L[3:], R1)
    elif L[:3] == [1, 1, 0]:
        compute_next([1, 0] + L[3:], R1)
    elif L[:3] == [1, 1, 1]:
        compute_next([1, 1] + L[3:], R1)