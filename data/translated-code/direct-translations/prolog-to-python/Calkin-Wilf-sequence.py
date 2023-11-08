```python
# John Devou: 26-Nov-2021

# g(N,X):- consecutively generate in X the first N elements of the Calkin-Wilf sequence
def g(N, X):
    if N > 0:
        X.append(1/1)
    if N > 1:
        Ls = [1/1]
        Ys = []
        for i in range(1, N):
            A, B = X[i-1].split("/")
            A, B = int(A), int(B)
            C = A + B
            X.append(A/B)
            Ls.append(A/B)
            Ls.append(A/C)
            Ys.append(C/B)
        g(N-1, Ls-Ys, X)

# t(A/B,X):- generate in X the index of A/B in the Calkin-Wilf sequence
def t(A, B, S=1, C=1):
    if B == 1:
        return C * (2**(A-1+S) - S)
    elif B > 1:
        M, N = divmod(A, B)
        T = 1 - S
        D = C * 2**M
        Y = t(B, N, T, D)
        return Y + S*C*(2**M - 1)
    
# example usage
result = []
g(5, result)
print(result)

index = t(5, 3)
print(index)
```