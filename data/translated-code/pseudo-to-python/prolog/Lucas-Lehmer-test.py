def show(Count):
    S = []
    for N in limit(Count, (between(2, infinite, N), mersenne_prime(N))):
        S.append(N)
    for P in S:
        write(P + " ")
    write("\n")

def lucas_lehmer_seq(M, L):
    lazy_list(ll_iter, 4-M, L)

def ll_iter(S-M, T-M, T):
    T = ((S*S) - 2) % M

def drop(N, Lz1, Lz2):
    Pfx = []
    for item in Lz1:
        if len(Pfx) == N:
            break
        Pfx.append(item)
    Lz2 = Pfx

def mersenne_prime(2):
    return True
def mersenne_prime(P):
    if P <= 2:
        return False
    if prime(P) is True:
        M = (1 << P) - 1
        Residues = lucas_lehmer_seq(M)
        Skip = P - 3
        drop(Skip, Residues, [R, _])
        if R == 0:
            return True
        else:
            return False

def wheel235(L):
    W = [4, 2, 4, 2, 4, 6, 2, 6]
    L = [1, 2, 2]
    for item in W:
        L.append(item)

def prime(N):
    if N < 2:
        return False
    W = wheel235()
    return prime_helper(N, 2, W)

def prime_helper(N, D, _):
    if D * D > N:
        return True
    if N % D != 0:
        return prime_helper(N, D + 2, _)
    else:
        return False