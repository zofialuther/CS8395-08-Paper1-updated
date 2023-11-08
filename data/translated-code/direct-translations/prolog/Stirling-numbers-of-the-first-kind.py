```python
stirling1_cache = {}

def stirling1(N, N, 1):
    return 1
def stirling1(_, 0, 0):
    return 0
def stirling1(N, K, L):
    if K > N:
        return 0
    if (N, K) in stirling1_cache:
        return stirling1_cache[(N, K)]
    else:
        N1 = N - 1
        K1 = K - 1
        L1 = stirling1(N1, K, L)
        L2 = stirling1(N1, K1, L)
        L = L2 + (N - 1) * L1
        stirling1_cache[(N, K)] = L
        return L

def print_stirling_numbers(N):
    for K in range(1, N+1):
        L = stirling1(N, K, 0)
        print(f'{L:10}', end='')
    print()

def print_stirling_numbers_up_to(M):
    for N in range(1, M+1):
        print_stirling_numbers(N)

def max_stirling1(N):
    max_val = 0
    for K in range(1, N+1):
        L = stirling1(N, K, 0)
        max_val = max(max_val, L)
    return max_val

def main():
    print('Unsigned Stirling numbers of the first kind up to S1(12,12):')
    print_stirling_numbers_up_to(12)
    print('Maximum value of S1(n,k) where n = 100:')
    M = max_stirling1(100)
    print(M)

main()
```