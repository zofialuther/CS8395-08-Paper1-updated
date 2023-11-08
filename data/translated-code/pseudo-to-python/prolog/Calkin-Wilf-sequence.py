def g(N, fraction, X):
    if N > 0:
        return fraction
    
def g(N, fraction_list, X):
    if N > 1:
        M = N - 1
        A = fraction_list[0][0]
        B = fraction_list[0][1]
        C = A + B
        g(M, fraction_list[1:] - fraction_list[2:], X)
        
def g(N, X):
    g(N, [(1, 1)] - [1], X)
    
def t(A, B, S, C, X):
    if B == 1:
        X = C * (2**(A - 1 + S) - S)
    else:
        M, N = divmod(A, B)
        T = 1 - S
        D = C * 2**M
        t(B, N, T, D, Y)
        X = Y + S * C * (2**M - 1)
        
def t(A, B, X):
    t(A, B, 1, 1, X)