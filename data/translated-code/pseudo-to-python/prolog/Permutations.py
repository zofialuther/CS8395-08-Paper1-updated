def permut_Prolog(P, L):
    if not P and not L:
        return True
    if P and not L:
        return False
    H = P[0]
    T = P[1:]
    NL1 = select(H, L)
    permut_Prolog(T, NL1)