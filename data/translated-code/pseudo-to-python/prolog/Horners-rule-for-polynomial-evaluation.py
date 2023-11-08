def horner(L, X):
    return 0 if len(L) == 0 else L[0] + X * horner(L[1:], X)