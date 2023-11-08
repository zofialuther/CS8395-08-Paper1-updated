```python
def ft_rows(Lz):
    lazy_list(ft_row, [], Lz)

def ft_row([], R1, R1):
    R1 = [1]

def ft_row(R0, R2, R2):
    P = len(R0)
    Jmax = 1 + P
    Qs = list(range(2, Jmax))
    R1 = list(map(term(P), Qs, R0))
    S = sum(R1)
    Bk = 1 - S
    R2 = [Bk] + R1

def term(P, Q, R):
    return R * (P / Q)

def show(N):
    ft_rows(Rs)
    Rows = len(Rs, N)
    prefix(Rows, Rs)
    for R in Rows:
        S = format("~w", [R])
        T = re_replace(" rdiv ", "/", S)
        U = re_replace(",", ", ", T)
        write(U)

def sum(N, K):
    ft_rows(Rows)
    Coefs = Rows[K:]
    Coefs = Coefs[::-1]
    Poly = [0] + Coefs
    S = foldl(horner(N), Poly, 0)

def horner(N, A, S0):
    return N * S0 + A

def drop(N, Lz1):
    Pfx = Lz1[:N]
    return Pfx
```