def msort(L, S):
    if not L:
        S = []
    elif len(L) == 1:
        S = L
    else:
        L, R = split(L)
        SL = msort(L)
        SR = msort(R)
        S = merge(SL, SR)
    return S

def split(L):
    if not L:
        return [], []
    elif len(L) == 1:
        return [L], []
    else:
        LT = [L[i] for i in range(len(L)) if i % 2 == 0]
        RT = [L[i] for i in range(len(L)) if i % 2 != 0]
        return LT, RT

def merge(LS, RS):
    if not LS:
        return RS
    elif not RS:
        return LS
    else:
        if LS[0] <= RS[0]:
            return [LS[0]] + merge(LS[1:], RS)
        else:
            return [RS[0]] + merge(LS, RS[1:])