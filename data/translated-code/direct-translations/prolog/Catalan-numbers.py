def catalan(N):
    L1 = [None] * N
    L = [1] + L1
    init(1, 1, L1)
    NL = list(range(0, N+1))
    for n in NL:
        my_write(n, L[n])

def init(_, _, []):
    pass

def init(V, N, T):
    if len(T) > 0:
        N1 = N + 1
        T[0] = 2 * (2 * N - 1) * V / N1
        init(T[0], N1, T[1:])

def my_write(N, V):
    print(f'{N} : {V}')