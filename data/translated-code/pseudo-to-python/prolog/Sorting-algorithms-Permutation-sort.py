def permutation_sort(L, S):
    permutation(L, S)
    sorted(S)

def sorted([]):
    pass

def sorted([_]):
    pass

def sorted([X, Y, *ZS]):
    if (X <= Y):
        sorted([Y, *ZS])

def permutation([], []):
    pass

def permutation([X, *XS], YS):
    permutation(XS, ZS)
    select(X, YS, ZS)