```python
def levenshtein(S, T, R):
    M = len(S)
    M1 = M + 1
    N = len(T)
    N1 = N + 1
    Lev = [0] * N1
    Lev = [Lev[:] for _ in range(M1)]
    LN = list(range(N))
    for i in range(N):
        Lev[i][0] = i
    for i in range(M):
        Lev[0][i] = i

    for i in range(1, N1):
        for j in range(1, M1):
            if T[i-1] == S[j-1]:
                cost = 0
            else:
                cost = 1
            Lev[i][j] = min(Lev[i-1][j] + 1, Lev[i][j-1] + 1, Lev[i-1][j-1] + cost)

    R = Lev[-1][-1]
```