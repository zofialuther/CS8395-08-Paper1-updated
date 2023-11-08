def unsigned_lah_number(N, K, cache):
    if N == K:
        return 1
    elif K == 0:
        return 0
    elif K > N:
        return 0
    else:
        if (N, K) in cache:
            return cache[(N, K)]
        else:
            L1 = unsigned_lah_number(N - 1, K, cache)
            L2 = unsigned_lah_number(N - 1, K - 1, cache)
            L = (N - 1 + K) * L1 + L2
            cache[(N, K)] = L
            return L

def print_unsigned_lah_numbers(N):
    cache = {}
    for K in range(1, N + 1):
        L = unsigned_lah_number(N, K, cache)
        print(L)

def max_unsigned_lah_number(N):
    Max = 0
    cache = {}
    for K in range(1, N + 1):
        L = unsigned_lah_number(N, K, cache)
        if L > Max:
            Max = L
    return Max

def main():
    print_unsigned_lah_numbers(12)
    M = max_unsigned_lah_number(100)
    print(M)

main()