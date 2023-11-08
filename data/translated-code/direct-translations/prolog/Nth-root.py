def iroot(_, 0, 0):
    return
def iroot(M, N, R):
    if M > 1:
        if N > 0:
            irootpos(M, N, R)
        else:
            if N & 1 == 1:
                NegN = -N
                irootpos(M, NegN, R0)
                R = -R0
def irootpos(N, A, R):
    X0 = 1 << (msb(A) // N)
    newton(N, A, X0, X1)
    iroot_loop(A, X1, N, A, R)
def iroot_loop(X1, X2, _, _, R):
    if X1 <= X2:
        return X1
    else:
        newton(N, A, X1, X2)
        iroot_loop(X1, X2, N, A, R)
def newton(2, A, X0, X1):
    return (X0 + A // X0) >> 1
def newton(N, A, X0, X1):
    return ((N - 1)*X0 + A // X0**(N - 1)) // N