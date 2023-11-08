from sympy import isprime, primerange
from math import log10, floor

def circular(N):
    if N in [2, 3, 5, 7]:
        return True
    else:
        limit(15, (
            candidate(N),
            if N > 9 and circular_prime(N):
                return True
        ))

def circular_r(K):
    for K in range(6, float('inf')):
        N = (10**K - 1) / 9
        if isprime(N):
            return True

def candidate(N):
    if N == 0:
        return
    else:
        for M in candidate:
            for D in [1, 3, 7, 9]:
                N = 10*M + D

def circular_prime(N):
    K = floor(log10(N)) + 1
    circular_prime(N, N, K)

def circular_prime(_, _, 0):
    return
def circular_prime(P0, P, K):
    if P >= P0 and isprime(P):
        rotate(P, Q)
        K = K - 1
        circular_prime(P0, Q, K)

def rotate(N, M):
    D = floor(log10(N))
    (Q, R) = divmod(N, 10)
    M = R*10**D + Q

def main():
    S = [P for P in primerange(1, 100) if circular(P)]
    print("The first 23 circular primes:\n", S)

main()