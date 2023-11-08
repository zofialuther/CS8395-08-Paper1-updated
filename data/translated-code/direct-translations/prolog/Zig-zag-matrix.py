def zig_zag(N):
    zig_zag(N, N)

def zig_zag(Lig, Col):
    M = [None] * Lig
    for i in range(Lig):
        M[i] = [None] * Col
    for i in range(Lig):
        for j in range(Col):
            M[i][j] = 0
    fill(M, 0, 0, 0, Lig, Col, "up")
    for line in M:
        print_line(line)

def fill(M, Cur, L, C, NL, NC, Sens):
    if L == NL - 1 and C == NC - 1:
        Line = M[L]
        Line[C] = Cur
    else:
        Line = M[L]
        Line[C] = Cur
        Cur1 = Cur + 1
        L1, C1, Sens1 = compute_next(NL, NC, L, C, Sens)
        fill(M, Cur1, L1, C1, NL, NC, Sens1)

def init(N, L):
    L = [None] * N

def compute_next(NL, NC, L, C, Sens):
    if Sens == "up":
        if C < NC - 1:
            return L, C+1, "down"
        elif C == NC - 1:
            return L, C, "down"
    elif Sens == "down":
        if L < NL - 1:
            return L+1, C, "up"
        elif L == NL - 1:
            return L, C+1, "up"

def print_line(L):
    for val in L:
        print_val(val)
    print("\n")

def print_val(V):
    print("{:3d} ".format(V))