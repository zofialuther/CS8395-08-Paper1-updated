from hiordlib import foldr

def horner(L, X):
    return foldr(lambda H, V0, V: V0*X + H, L, 0)