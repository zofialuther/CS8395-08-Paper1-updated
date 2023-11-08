def wheel235(L):
    W = [6, 4, 2, 4, 2, 4, 6, 2]
    W.extend(W)
    L = accumulate(1/W, L)

def accumulate(M_A, N_As, N):
    N = M + A

def roll235wheel(Limit, A):
    wheel235(W)
    A = W[:-1]
    N = A[-1]
    if N > Limit:
        return

def prime235(N):
    wheel235(W)
    wheel_prime(N, W)

def wheel_prime(N, Ds):
    if D*D > N:
        return
    else:
        if N % D != 0:
            return wheel_prime(N, Ds[1:])

def primes(Limit, Primes):
    roll235wheel(Limit, Candidates)
    Primes = list(filter(prime235, Candidates))