def sierpinski_triangle(N):
    Len = 2 ** (N+1) - 1
    L = [None] * Len
    LN = list(range(1, Len+1))
    for i in range(Len):
        L[i] = init(N, LN[i])
    Line = ''.join(L)
    print(Line)
    NbTours = 2**N - 1
    loop(NbTours, LN, Len, L)

def init(N, Num):
    if 2 ** N + 1 == Num:
        return '*'
    else:
        return ' '

def loop(N, LN, Len, L):
    if N == 0:
        return
    else:
        L1 = list(map(lambda x: compute_next_line(Len, L, x), LN))
        Line = ''.join(L1)
        print(Line)
        loop(N-1, LN, Len, L1)

def compute_next_line(Len, L, I):
    I1 = I - 1
    I2 = I + 1
    V0 = ' ' if I == 1 else L[I1-1]
    V1 = L[I-1]
    V2 = ' ' if I == Len else L[I2-1]
    return rule_90(V0, V1, V2)

def rule_90(V0, V1, V2):
    if (V0, V1, V2) in [('*', '*', '*', ' '), ('*', '*', ' ', '*'), ('*', ' ', '*', ' '), ('*', ' ', ' ', '*'), (' ', '*', '*', '*'), (' ', '*', ' ', ' '), (' ', ' ', '*', '*'), (' ', ' ', ' ', ' ')]:
        return ' '
    else:
        return '*'
    