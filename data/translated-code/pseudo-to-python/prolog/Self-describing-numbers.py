def self_describling():
    for I in range(1, 11):
        L = findall(N, self_describling(I,N))
        print("Len", I, "Numbers", L)

def self_describling(Len, N):
    L = [0] * Len
    Len1 = Len - 1
    H = L[0]
    T = L[1:]
    H in range(1, Len1+1)
    Len2 = Len - 2
    T in range(0, Len2+1)
    sum(L) = Len
    H1 = H + 1
    V = L[H1]
    V > 0
    label(L)
    L.sort()
    packList(L, LNP)
    NumList = list(range(0, Len1+1))
    verif(LNP, NumList, L)
    convert(L, N)

def self_describling(N):
    L = list(str(N))
    L.sort()
    packList(L, LNP)
    Len = len(L)
    NumList = list(range(0, Len+1))
    verif(LNP, NumList, L)

def verif([], [], []):
    return True

def verif([], [N, *S], [0, *T]):
    return verif([], S, T)

def verif([[V, N], *R], [N, *S], [V, *T]):
    return verif(R, S, T)

def verif([[V, N1], *R], [N, *S], [0, *T]):
    if N < N1:
        return verif([[V,N1], *R], S, T)

def packList([],[]):
    return True

def packList([X], [[1, X]]):
    return True

def packList([X, *Rest], [XRun, *Packed]):
    run(X, Rest, XRun, RRest)

def run(Var, [], [1, Var], []):
    return True

def run(Var, [Var, *LRest], [N1, Var], RRest):
    if N > 0:
        N1 = N + 1
        run(Var, LRest, [N, Var], RRest)

def run(Var, [Other, *RRest], [1, Var], [Other, *RRest]):
    if Var != Other:
        return True