def egcd(_, 0, 1, 0):
    return

def egcd(A, B, X, Y):
    if B == 0:
        return 1, 0
    else:
        Q, R = divmod(A, B)
        S, X = egcd(B, R)
        Y = S - Q * X
        return X, Y

def modinv(A, B, N):
    X, Y = egcd(A, B)
    if A*X + B*Y == 1:
        N = X % B
        return N