```python
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("stirling2_cache(_, _, _)")

def stirling2(N, N, 1):
    return 1
def stirling2(_, 0, 0):
    return 0
def stirling2(N, K, L):
    if K > N:
        return 0
    return L
def stirling2(N, K, L):
    N1 = N - 1
    K1 = K - 1
    L1 = stirling2(N1, K)
    L2 = stirling2(N1, K1)
    L = K * L1 + L2
    prolog.assertz("stirling2_cache({}, {}, {})".format(N, K, L))

def print_stirling_numbers(N):
    for K in range(1, N+1):
        L = stirling2(N, K)
        print('{:8d}'.format(L))
def print_stirling_numbers_up_to(M):
    for N in range(1, M+1):
        print_stirling_numbers(N)

def max_stirling2(N):
    Max = max(stirling2(N, K) for K in range(1, N+1))
    return Max

print('Stirling numbers of the second kind up to S2(12,12):')
print_stirling_numbers_up_to(12)
print('Maximum value of S2(n,k) where n = 100:')
print(max_stirling2(100))
```