def divcount(N, Count):
    divcount_helper(N, 1, 0, Count)

def divcount_helper(N, D, C, Count):
    if D*D > N:
        Count = C
    else:
        D2 = D + 1
        A = divs(N, D)
        C2 = A + C
        divcount_helper(N, D2, C2, Count)

def divs(N, D):
    if N % D != 0:
        return 0
    elif D*D == N:
        return 1
    else:
        return 2

def antiprimes(N, L):
    antiprimes_helper(N, 1, 0, [], L)

def antiprimes_helper(N, M, Max, L, R):
    if N == 0:
        R = L[::-1]
    else:
        Count = divcount(M)
        M2 = M + 1
        if Count > Max:
            N0 = N - 1
            antiprimes_helper(N0, M2, Count, [M] + L, R)
        else:
            antiprimes_helper(N, M2, Max, L, R)

def main():
    X = []
    antiprimes(20, X)
    print("The first twenty anti-primes are ", X)

main()