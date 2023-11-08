import math
from itertools import product

def circular(N):
    if N in [2, 3, 5, 7]:
        return True
    elif limit(15, (candidate(N)) and N > 9 and circular_prime(N)):
        return True
    else:
        return False

def candidate(n):
    if n == 0:
        return True
    else:
        for m in candidate:
            for d in [1, 3, 7, 9]:
                if n == 10 * m + d:
                    return True
    return False
    
def circular_prime(N):
    K = math.floor(math.log10(N)) + 1
    return circular_prime(N, N, K)

def circular_prime(P0, P, K):
    if P0 <= P and prime(P):
        Q = rotate(P)
        if K > 0:
            return circular_prime(P0, Q, K - 1)
    return False

def rotate(N):
    D = math.floor(math.log10(N))
    Q = N // 10
    R = N % 10
    M = R * 10 ** D + Q
    return M

def main():
    S = [P for P in limit(23, circular(P))]
    print("The first 23 circular primes:\n", S)

main()