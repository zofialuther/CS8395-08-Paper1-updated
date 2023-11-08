def mersenne_factor(P, F):
    if prime(P):
        for K in range(1, 100001):
            Q = 2 * K * P + 1
            if test_factor(Q, P, F):
                return True
    return False

def test_factor(Q, P, F):
    if Q*Q > (1 << P - 1):
        return True
    else:
        R = Q % 7
        if R == 1 or R == 7:
            if prime(Q) and powm(2, P, Q) == 1:
                F = Q
                return True
    return False

def wheel235(L):
    W = [4, 2, 4, 2, 4, 6, 2, 6]
    W += W  # Repeats W infinitely
    L = [1, 2, 2] + W

def prime(N):
    if N >= 2:
        W = wheel235(W)
        return prime(N, 2, W)

def prime(N, D, W):
    if D*D > N:
        return True
    else:
        if N % D != 0:
            A = W.pop(0)
            D2 = D + A
            return prime(N, D2, W)