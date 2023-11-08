def ft_rows(Lz):
    lazy_list(ft_row, [], Lz)

def ft_row(R0, R2, R2):
    if R0 == []:
        R1 = [1]
        R2 = R1
    else:
        P = len(R0)
        Jmax = 1 + P
        Qs = list(range(2, Jmax))
        R1 = list(map(lambda Q: term(P, Q, R0, R1), Qs))
        S = sum(R1)
        Bk = 1 - S
        R2 = [Bk] + R1

def term(P, Q, R, S):
    S = R * (P / Q)

def show(N):
    Rs = ft_rows()
    Rows = [None] * N
    prefix(Rows, Rs)
    for R in Rows:
        S = str(R)
        S = S.replace(" rdiv ", "/")
        S = S.replace(",", ", ")
        print(S)

def sum(N, K, S):
    Rows = ft_rows()
    Coefs = drop(K, Rows)[0]
    Poly = [0] + Coefs
    Poly.reverse()
    S = 0
    for A in Poly:
        S = N * S + A

def drop(N, Lz1):
    Pfx = Lz1[:N]
    return Pfx