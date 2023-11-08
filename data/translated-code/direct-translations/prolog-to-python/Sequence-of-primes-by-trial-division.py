```python
def wheel235(L):
    W = [6, 4, 2, 4, 2, 4, 6, 2] + W
    lazy_list(accumulate, 1/W, L)

def accumulate(M_A, N_As, N):
    N = M_A[0] + N_As[0]

def roll235wheel(Limit, A):
    wheel235(W)
    A = A + [N for N in W if N > Limit]

def prime235(N):
    wheel235(W)
    wheel_prime(N, W)

def wheel_prime(N, Ds):
    for D in Ds:
        if D*D > N:
            return
        if N % D != 0:
            wheel_prime(N, Ds)

def primes(Limit, Primes):
    Candidates = roll235wheel(Limit)
    Primes = [N for N in Candidates if prime235(N)]
    Primes = [2, 3, 5] + Primes
```