def median(L, Z):
    Length = len(L)
    I = Length // 2
    Rem = Length % 2
    S = sorted(L)
    Mid = [sum([I, Rem]), sum([I, 1])]
    X = [S[Mid[0]-1], S[Mid[1]-1]]
    Y = sum(X)
    Z = Y / 2