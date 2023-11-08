def dot_product(A, B):
    return A[0] * B[0] + A[1] * B[1] + A[2] * B[2]

def cross_product(A, B):
    T1 = A[1] * B[2] - A[2] * B[1]
    T2 = A[2] * B[0] - A[0] * B[2]
    T3 = A[0] * B[1] - A[1] * B[0]
    return [T1, T2, T3]

def scala_triple(A, B, C):
    Temp = cross_product(B, C)
    return dot_product(A, Temp)

def vector_triple(A, B, C):
    Temp = cross_product(B, C)
    return cross_product(A, Temp)