def zig_zag(N):
    zig_zag(N, N)

def zig_zag(Lig, Col):
    M = [[0] * Col for _ in range(Lig)]
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
        compute_next(NL, NC, L, C, Sens, L1, C1, Sens1)
        fill(M, Cur1, L1, C1, NL, NC, Sens1)

def compute_next(NL, NC, Lig, Col, Sens, Lig1, Col1, Sens1):
    if Sens == "up" and Col < NC - 1:
        Col1 = Col + 1
        Sens1 = "down"
    elif Sens == "up" and Col == NC - 1:
        Col1 = Col
        Sens1 = "down"
    elif Sens == "down" and Lig < NL - 1:
        Lig1 = Lig + 1
        Col1 = Col - 1
        Sens1 = "down"
    elif Sens == "down" and Lig == NL - 1:
        Lig1 = Lig
        Col1 = Col + 1
        Sens1 = "up"
    elif Sens == "up" and Col < NC - 1:
        Lig1 = Lig - 1
        Col1 = Col + 1
        Sens1 = "up"
    elif Sens == "up" and Col == NC - 1:
        Lig1 = Lig + 1
        Col1 = Col
        Sens1 = "down"

def print_line(L):
    for value in L:
        print_val(value)
    print("\n")

def print_val(V):
    print("{:3}".format(V), end="")