def stirling2(N, K, L):
    if K == N == 1:
        return 1
    elif K == 0 or K > N:
        return 0
    elif L == 0:
        return stirling2(N-1, K-1, 0) + K * stirling2(N-1, K, 0)
    else:
        return L

def print_stirling_numbers(N):
    for K in range(1, N+1):
        L = stirling2(N, K, 0)
        print(L, end=" ")
    print()

def print_stirling_numbers_up_to(M):
    for N in range(1, M+1):
        print_stirling_numbers(N)

def max_stirling2(N):
    max_val = 0
    for n in range(1, N+1):
        for k in range(1, n+1):
            L = stirling2(n, k, 0)
            max_val = max(max_val, L)
    return max_val

print("Stirling numbers of the second kind up to S2(12,12):")
print_stirling_numbers_up_to(12)
print("Maximum value of S2(n,k) where n = 100:")
print(max_stirling2(100))