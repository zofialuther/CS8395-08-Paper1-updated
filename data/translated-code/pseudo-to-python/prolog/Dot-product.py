def dot_product(L1, L2, N):
    P = []
    for i in range(len(L1)):
        P.append(L1[i] * L2[i])
    N = sum(P)