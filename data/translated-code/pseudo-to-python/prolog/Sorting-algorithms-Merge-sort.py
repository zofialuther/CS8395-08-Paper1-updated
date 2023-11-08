def msort(L, S):
    if len(L) == 0:
        S = []
    elif len(L) == 1:
        S = L
    else:
        L1, L2 = split(L)
        S1 = msort(L1, [])
        S2 = msort(L2, [])
        merge(S1, S2, S)

def split(LIST):
    if len(LIST) == 0:
        return [], []
    elif len(LIST) == 1:
        return LIST, []
    else:
        L = LIST[0]
        R = LIST[1]
        LT, RT = split(LIST[2:])
        return [L] + LT, [R] + RT

def merge(LS, RS, M):
    if len(LS) == 0:
        M = RS
    elif len(RS) == 0:
        M = LS
    elif LS[0] <= RS[0]:
        M = [LS[0]]
        merge(LS[1:], RS, M)
    else:
        M = [RS[0]]
        merge(LS, RS[1:], M)