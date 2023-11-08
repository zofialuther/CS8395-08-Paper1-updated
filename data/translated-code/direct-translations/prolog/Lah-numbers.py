```python
cache = {}

def unsigned_lah_number(N, K):
    if (N, K) in cache:
        return cache[(N, K)]
    if N == K:
        return 1
    if K == 0:
        return 0
    if K > N:
        return 0
    L1 = unsigned_lah_number(N-1, K)
    L2 = unsigned_lah_number(N-1, K-1)
    result = (N-1+K) * L1 + L2
    cache[(N, K)] = result
    return result

def print_unsigned_lah_numbers(N):
    for K in range(1, N+1):
        L = unsigned_lah_number(N, K)
        print(f'{L:11}', end='')
    print()

def max_unsigned_lah_number(N):
    max_val = max(unsigned_lah_number(N, K) for K in range(1, N+1))
    return max_val

print('Unsigned Lah numbers up to L(12,12):')
for N in range(1, 13):
    print_unsigned_lah_numbers(N)
print('Maximum value of L(n,k) where n = 100:')
print(max_unsigned_lah_number(100))
```