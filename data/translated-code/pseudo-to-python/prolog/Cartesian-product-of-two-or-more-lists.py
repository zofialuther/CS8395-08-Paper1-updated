def product(A, Bs, X):
    if A:
        A_head = A[0]
        X = [(A_head, B) for B in Bs]
        return X
    else:
        A_tail = A[1:]
        X = product(A_tail, Bs, X)
        return X