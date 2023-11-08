def accRev(L, A, R):
    if len(L) != 0:
        accRev(L[1:], [L[0]] + A, R)
    else:
        R.extend(A)

def rev(L, R):
    accRev(L, [], R)