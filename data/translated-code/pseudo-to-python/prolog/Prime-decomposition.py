def wheel2357(L):
    W = [2,  4,  2,  4,  6,  2,  6,  4,
         2,  4,  6,  6,  2,  6,  4,  2,
         6,  4,  6,  8,  4,  2,  4,  2,
         4,  8,  6,  4,  6,  2,  4,  6,
         2,  6,  6,  4,  2,  4,  6,  2,
         6,  4,  2,  4,  2, 10,  2, 10]
    L = [1, 2, 2, 4] + W

def factor(N, Fac):
    if (N == 1):
        return 1
    W = wheel2357()
    return factor(N, 2, W, 1, Fac0)

def factor(N, F, W, Fac1, Fac2):
    if (F*F > N):
        return addFactor(N, Fac1, Fac2)
    if (N % F == 0):
        Q = N / F
        Fac2 = addFactor(F, Fac1)
        return factor(Q, F, W, Fac2, Fac)
    F2 = F + W[0]
    return factor(N, F2, W[1:], Fac1, Fac)

def addFactor(F, Fac1, Fac2):
    if (Fac1 == 1):
        return F
    elif (Fac1 == F):
        return F**2
    else:
        return F * Fac1

def reverseFactors(A, B, C):
    if (A * B == C):
        return reverseFactors(B, C, A)
    else:
        return A