def kaprekar_(Z, X):
    split_number(Z, 10, X)

def split_number(Z, N, X):
    if N < Z:
        A = Z // N
        B = Z % N
        if X == A + B and B != 0:
            return True
        else:
            N1 = N * 10
            return split_number(Z, N1, X)

def kaprekar(N, V):
    for X in range(1, N+1):
        Z = X * X
        if Z == X * X:
            if kaprekar_(Z, X):
                V.append(X)
        elif X == 1:
            V.append(X)