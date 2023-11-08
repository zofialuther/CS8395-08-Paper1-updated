def tt_divisors(X, N, TT):
    Q = X // N
    if (X % N == 0):
        if (Q == N):
            TT1 = N + TT
        else:
            TT1 = N + Q + TT
    else:
        TT1 = TT
    if (X ** 0.5 > N + 1):
        N1 = N + 1
        tt_divisors(X, N1, TT1)
    else:
        TT1 = X

def perfect(X):
    tt_divisors(X, 2, 1)

def perfect_numbers(N, L):
    LN = list(range(2, N))
    L = list(filter(perfect, LN))