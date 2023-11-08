def qsort(arr, S):
    if arr == []:
        return []
    else:
        H = arr[0]
        U = arr[1:]
        L, R = splitBy(H, U, [], [])
        SL = qsort(L, [])
        SR = qsort(R, [])
        return SL + [H] + SR

def splitBy(H, U, LS, RS):
    if U == []:
        return LS, RS
    else:
        if U[0] <= H:
            LS.append(U[0])
        else:
            RS.append(U[0])
        return splitBy(H, U[1:], LS, RS)