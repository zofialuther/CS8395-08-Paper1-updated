def divcount(N, Count):
    divcount(N, 1, 0, Count)

def divcount(N, D, C, C):
    if D*D > N:
        return
    else:
        D2 = D + 1
        A = divs(N, D)
        C2 = A + C
        divcount(N, D2, C2, C)

def divs(N, D):
    if N % D != 0:
        return 0
    elif D*D == N:
        return 1
    else:
        return 2

def antiprimes(N, L):
    antiprimes(N, 1, 0, [], L)

def antiprimes(N, M, Max, L, R):
    if N == 0:
        R = L[::-1]
        return
    else:
        Count = divcount(M)
        M2 = M + 1
        if Count > Max:
            N0 = N - 1
            antiprimes(N0, M2, Count, L + [M], R)
        else:
            antiprimes(N, M2, Max, L, R)

def main():
    X = antiprimes(20)
    print("The first twenty anti-primes are ", X)

main()