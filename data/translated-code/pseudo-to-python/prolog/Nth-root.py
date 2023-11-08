def iroot(M, N, R):
    if N == 0:
        return 0
    if M > 1:
        if N > 0:
            return irootpos(M, N, R)
        else:
            if N % 2 == 1:
                NegN = -N
                R0 = irootpos(M, NegN)
                return -R0

def irootpos(N, A):
    X0 = 1 << (A.bit_length() // N)
    X1 = newton(N, A, X0)
    return iroot_loop(X0, X1, N, A)

def iroot_loop(X1, X2, N, A):
    if X1 <= X2:
        return X1
    else:
        X2 = newton(N, A, X1)
        return iroot_loop(X1, X2, N, A)

def newton(N, A, X0):
    if N == 2:
        X1 = (X0 + A // X0) >> 1
        return X1
    else:
        X1 = ((N - 1) * X0 + A // (X0 ** (N - 1))) // N
        return X1