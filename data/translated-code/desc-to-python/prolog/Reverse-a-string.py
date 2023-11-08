def accRev([H|T], A):
    if T == []:
        return [H] + A
    else:
        return accRev(T, [H] + A)

def rev(L):
    return accRev(L, [])