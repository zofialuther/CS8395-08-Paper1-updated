```python
def show():
    Data = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    for Max in Data:
        Total, Prim = count_triples(Max)
        print("upto {}, there are {} Pythagorean triples ({} primitive.)".format(Max, Total, Prim))


def div(A, B, C):
    C = A // B


def count_triples(Max):
    Ps = []
    for A in range(Max):
        for B in range(Max):
            for C in range(Max):
                if A**2 + B**2 == C**2 and A + B + C <= Max:
                    Ps.append(A + B + C)
    Prims = len(Ps)
    Counts = [Max / ps for ps in Ps]
    Total = sum(Counts)
    return Total, Prims


def between_by(A, B, N, K):
    C = (B - A) // N
    for J in range(C + 1):
        if N * J + A <= B:
            K = N * J + A


def triple(P, A, B, C):
    Max = int((P / 2)**0.5) - 1
    for M in range(Max + 1):
        Start = (M & 1) + 1
        Pm = M + 1
        N = between_by(Start, Pm, 2)
        if gcd(M, N) == 1:
            X = M**2 - N**2
            Y = 2 * M * N
            C = M**2 + N**2
            order2(X, Y, A, B)
            if A + B + C <= P:
                return A, B, C


def order2(A, B, C, D):
    if A < B:
        return A, B
    else:
        return B, A
```