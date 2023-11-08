def levenshtein(S, T, R):
    M = len(S)
    M1 = M + 1
    N = len(T)
    N1 = N + 1
    Lev = [[0 for j in range(M1)] for i in range(N1)]
    
    LN = [i for i in range(N)]

    for i in range(N):
        Lev[i][0] = i
    
    for i in range(M):
        Lev[0][i] = i
    
    for i in range(1, N1):
        for j in range(1, M1):
            if T[i-1] == S[j-1]:
                Lev[i][j] = Lev[i-1][j-1]
            else:
                VD = Lev[i][j-1] + 1
                VI = Lev[i-1][j] + 1
                VS = Lev[i-1][j-1] + 1
                V = min(VD, VI, VS)
                Lev[i][j] = V
    
    R = Lev[N][M]