def dot_product(L1, L2, N):
    P = [a * b for a, b in zip(L1, L2)]
    total = sum(P)
    return total == N