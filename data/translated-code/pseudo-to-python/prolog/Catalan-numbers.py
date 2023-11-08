def catalan(N):
    L1 = [0] * N
    L = [1] + L1
    init(1, 1, L)
    NL = list(range(N))
    for number in NL:
        my_write(number, L)

def init(V, N, L):
    if not L:
        return
    else:
        N1 = N + 1
        H = 2 * (2 * N - 1) * V / N1
        init(H, N1, L)

def my_write(N, V):
    print(f"{N} : {V}")