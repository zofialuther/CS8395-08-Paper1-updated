def permut_Prolog(P, L):
    if P == [] and L == []:
        return True
    elif P != [] and L != []:
        H = P[0]
        T = P[1:]
        index = L.index(H)
        NL = L[:index] + L[index+1:]
        return permut_Prolog(T, NL)
    else:
        return False