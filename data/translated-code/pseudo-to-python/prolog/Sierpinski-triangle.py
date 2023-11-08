def sierpinski_triangle(N):
    Len = 2 ** (N + 1) - 1
    L = ['' for i in range(Len)]
    LN = [i for i in range(1, Len + 1)]
    for i in range(len(L)):
        L[i] = init(N, L[i], LN[i])
    Line = ''.join(L)
    print(Line)
    NbTours = 2 ** N - 1
    loop(NbTours, LN, Len, L)

def init(N, Cell, Num):
    if Num == 2 ** N + 1:
        Cell = '*'
    else:
        Cell = ' '
    return Cell

def loop(N, LN, Len, L):
    if N == 0:
        return
    L1 = ['' for i in range(Len)]
    for i in range(len(L)):
        L1[i] = compute_next_line(Len, L, LN[i], L1[i])
    Line = ''.join(L1)
    print(Line)
    N1 = N - 1
    loop(N1, LN, Len, L1)

def compute_next_line(Len, L, I, V):
    I1 = I - 1
    I2 = I + 1
    if I == 1:
        V0 = ' '
    else:
        V0 = L[I1 - 1]
    V1 = L[I - 1]
    if I == Len:
        V2 = ' '
    else:
        V2 = L[I2 - 1]
    return rule_90(V0, V1, V2, V)

def rule_90(V0, V1, V2, V):
    if V0 == '*' and V1 == '*' and V2 == '*':
        return ' '
    elif V0 == '*' and V1 == '*' and V2 == ' ':
        return '*'
    elif V0 == '*' and V1 == ' ' and V2 == '*':
        return ' '
    elif V0 == '*' and V1 == ' ' and V2 == ' ':
        return '*'
    elif V0 == ' ' and V1 == '*' and V2 == '*':
        return '*'
    elif V0 == ' ' and V1 == '*' and V2 == ' ':
        return ' '
    elif V0 == ' ' and V1 == ' ' and V2 == '*':
        return '*'
    elif V0 == ' ' and V1 == ' ' and V2 == ' ':
        return ' '