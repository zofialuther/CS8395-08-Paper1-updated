def show(Count):
    S = [N for N in range(2, Count + 1) if mersenne_prime(N)]
    for P in S:
        print(P, end=" ")
    print()

def lucas_lehmer_seq(M, L):
    L = ll_iter(4 - M)

def ll_iter(S_M):
    T_M = (S*S - 2) % M
    return T_M

def drop(N, Lz1, Lz2):
    for i in range(len(Lz1)):
        if Lz1[i:i + len(Lz2)] == Lz2:
            return Lz1[i + len(Lz2):]

def mersenne_prime(P):
    if P == 2:
        return True
    elif P > 2 and prime(P):
        M = (1 << P) - 1
        Residues = lucas_lehmer_seq(M)
        Skip = P - 3
        if drop(Skip, Residues, [R]) == [0]:
            return True
    return False

def wheel235(L):
    W = [4, 2, 4, 2, 4, 6, 2, 6]
    L = [1, 2, 2] + W

def prime(N):
    if N >= 2:
        W = []
        wheel235(W)
        return prime(N, 2, W)

def prime(N, D, As):
    if D*D > N:
        return True
    elif N % D != 0:
        D2 = D + As[0]
        return prime(N, D2, As)