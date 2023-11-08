import heapq
import random
import math

def singleton_heap(H, value, nothing):
    H = []
    heapq.heappush(H, value)
    return H

def lazy_list(next_3smooth, value, Lz):
    Lz = []
    Lz.append(value)
    return Lz

def min_of_heap(H0, Top, _):
    Top = heapq.heappop(H0)
    return Top

def get_from_heap(H0, Top, _, H1):
    H1 = heapq.heappop(H0)
    return H1

def add_to_heap(H1, N2, nothing, H2):
    heapq.heappush(H1, N2)
    return H1

def first_kind(K):
    Ns = three_smooth()
    for N in Ns:
        if N + 1 == K and prime(K):
            return K

def second_kind(K):
    Ns = three_smooth()
    for N in Ns:
        if N - 1 == K and prime(K):
            return K

def show(Seq, N):
    print(f"The first {N} values of {Seq} are: ")
    L = []
    for X in Seq:
        if len(L) < N:
            L.append(X)
    print(L)
    TwoFifty = Seq[249]
    print(f"The 250th value of {Seq} is {TwoFifty}")

def main():
    show(first_kind, 50)
    show(second_kind, 50)
    return

def divcheck(N, Ps, Result):
    if len(Ps) == 0:
        return "unknown"
    elif Ps[0]*Ps[0] > N:
        return "prime"
    elif N % Ps[0] != 0:
        return Result

def miller_rabin_primality_test(N):
    Bases = bases(N)
    for A in Bases:
        if strong_fermat_pseudoprime(N, A) == False:
            return False
    return True

def bases(N):
    if N < 9080191:
        return [31, 73]
    elif N < 4759123141:
        return [2, 7, 61]
    elif N < 18446744073709551616:
        T = miller_rabin_precision(16)
        RndLimit = N - 2
        Bases = []
        for _ in range(T):
            Bases.append(random.randint(2, RndLimit))
        return Bases

def strong_fermat_pseudoprime(N, A):
    Pn = N + 1
    S, D = factor_2s(Pn)
    X = pow(A, D, N)
    if X == 1:
        return True
    else:
        if composite_witness(N, S, X) == False:
            return True
    return False

def composite_witness(N, K, X):
    if K == 0:
        return False
    else:
        if X != N-1:
            if composite_witness(N, K-1, (X*X) % N) == False:
                return False
    return True

def factor_2s(S, D):
    if D & 1 != 0:
        return S, D
    else:
        return factor_2s(S+1, D>>1)

def prime(N):
    if isinstance(N, int) and N > 1:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
        result = divcheck(N, primes, "prime")
        if result == "prime":
            return True
        elif miller_rabin_primality_test(N):
            return True
    return False

main()