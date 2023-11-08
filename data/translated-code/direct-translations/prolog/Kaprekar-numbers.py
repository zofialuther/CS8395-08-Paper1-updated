def kaprekar_(Z, X):
    split_number(Z, 10, X)

def split_number(Z, N, X):
    if N < Z:
        A = Z // N
        B = Z % N
        if (X == A+B) and (B != 0):
            return True
        else:
            N1 = N * 10
            split_number(Z, N1, X)

def kaprekar(N, V):
    result = []
    for X in range(1, N+1):
        Z = X * X
        if Z == 1:
            result.append(X)
        else:
            kaprekar_(Z, X)
    V = result