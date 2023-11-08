def roots(N, Rs):
    Pn = N + 1
    Ks = list(range(Pn))
    maplist(root(N), Ks, Rs)

def root(N, M, R2):
    R0 = (2 * M) / N
    if R0 > 1: 
        R1 = R0 - 2
    else: 
        R1 = R0
    cis(R1, R2)

def cis(0, 1):
    return
def cis(1, -1):
    return
def cis(1 / 2, "i"):
    return
def cis(-1 / 2, "-i"):
    return
def cis(-1 / Q, exp(-i * pi / Q)):
    return
def cis(1 / Q, exp(i * pi / Q)):
    return
def cis(P / Q, exp(P * i * pi / Q)):
    return