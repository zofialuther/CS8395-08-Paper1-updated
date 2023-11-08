```python
stirling1_cache = {}

def stirling1(N, N, 1):
    if N == N:
        return 1
    else:
        return

def stirling1(_, 0, 0):
    if _ == 0:
        return 0
    else:
        return

def stirling1(N, K, 0):
    if K > N:
        return 0
    else:
        return

def stirling1(N, K, L):
    if (N, K, L) in stirling1_cache:
        return
    else:
        return

def stirling1(N, K, L):
    N1 = N - 1
    K1 = K - 1
    L1 = stirling1(N1, K, L1)
    L2 = stirling1(N1, K1, L2)
    L = L2 + (N - 1) * L1
    stirling1_cache[(N, K, L)] = True

def print_stirling_numbers(N):
    for K in range(1, N + 1):
        L = stirling1(N, K, 0)
        print(L)
    return

def print_stirling_numbers(_):
    print("\n")
    return

def print_stirling_numbers_up_to(M):
    for N in range(1, M + 1):
        print_stirling_numbers(N)
    return

def max_stirling1(N, Max):
    Max = max(stirling1(N, K, L) for L in range(1, N + 1))
    return Max

def main():
    print("Unsigned Stirling numbers of the first kind up to S1(12,12):")
    print_stirling_numbers_up_to(12)
    print("Maximum value of S1(n,k) where n = 100:")
    M = None
    max_stirling1(100, M)
    print(M)
    return

main()
```