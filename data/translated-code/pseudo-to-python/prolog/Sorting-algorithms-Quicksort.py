def qsort(array, result):
    if len(array) == 0:
        return result
    else:
        H = array[0]
        U = array[1:]
        split = splitBy(H, U)
        L = split[0]
        R = split[1]
        SL = qsort(L, [])
        SR = qsort(R, [])
        return SL + [H] + SR

def splitBy(H, U):
    LS = []
    RS = []
    if len(U) == 0:
        return [LS, RS]
    else:
        first = U[0]
        rest = U[1:]
        if first <= H:
            LS.append(first)
        else:
            RS.append(first)
        splitRest = splitBy(H, rest)
        return [LS + splitRest[0], RS + splitRest[1] ]