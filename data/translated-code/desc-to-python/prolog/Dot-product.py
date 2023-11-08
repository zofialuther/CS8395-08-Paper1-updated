def dot_product(L1, L2, N):
    P = [mult(x, y) for x, y in zip(L1, L2)]
    return sumlist(P, N)

def mult(x, y):
    return x * y

def sumlist(lst, N):
    return sum(lst) == N