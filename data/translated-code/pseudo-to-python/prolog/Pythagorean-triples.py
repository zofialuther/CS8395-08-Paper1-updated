```python
def show():
    Data = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    for Max in Data:
        Total, Prim = count_triples(Max)
        print(f"upto {Max}, there are {Total} Pythagorean triples ({Prim} primitive.)")

def div(A, B, C):
    return A // B

def count_triples(Max):
    Ps = [A + B + C for (A, B, C) in triple(Max)]
    Prims = len(Ps)
    Counts = [div(Max, p) for p in Ps]
    Total = sum(Counts)
    return Total, Prims

def between_by(A, B, N, K):
    C = (B - A) // N
    for J in range(C + 1):
        if N*J + A == K:
            return True
    return False

def triple(P):
    Max = int(P**0.5 / 2) - 1
    triples = []
    for M in range(Max + 1):
        Start = (M & 1) + 1
        Pm = M + 1
        for N in range(Start, Pm, 2):
            if gcd(M, N) == 1:
                X = M**2 - N**2
                Y = 2*M*N
                C = M**2 + N**2
                A, B = order2(X, Y)
                if A + B + C <= P:
                    triples.append((A, B, C))
    return triples

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def order2(A, B):
    if A < B:
        return A, B
    else:
        return B, A
```