def compute_next(L, LN):
    if L == [0, 0, 0]:
        LN = [0, 0]
    elif L == [0, 0, 1]:
        LN = [0, 0]
    elif L == [0, 1, 0]:
        LN = [0, 0]
    elif L == [0, 1, 1]:
        LN = [0, 1]
    elif L == [1, 0, 0]:
        LN = [0, 0]
    elif L == [1, 0, 1]:
        LN = [1, 0]
    elif L == [1, 1, 0]:
        LN = [1, 0]
    elif L == [1, 1, 1]:
        LN = [0, 0]
    return LN

def one_dimensional_cellular_automata(L):
    print(L)
    length = len(L)
    LN = [0] * length
    LN = compute_next([0, L[0], L[1]], LN)
    for i in range(2, length):
        LN = compute_next([L[i-2], L[i-1], L[i]], LN)
    if L != LN:
        one_dimensional_cellular_automata(LN)

L = [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
one_dimensional_cellular_automata(L)