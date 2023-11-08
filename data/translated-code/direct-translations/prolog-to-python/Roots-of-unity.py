def roots(N):
    Pn = N + 1
    Ks = list(range(Pn))
    Rs = list(map(lambda x: root(N, x), Ks))
    return Rs

def root(N, M):
    R0 = (2 * M) / N
    if R0 > 1:
        R1 = R0 - 2
    else:
        R1 = R0
    return cis(R1)

def cis(x):
    if x == 0:
        return 1
    elif x == 1:
        return -1
    elif x == 1/2:
        return 'i'
    elif x == -1/2:
        return '-i'
    elif x < 0:
        return 'exp(-i*pi/' + str(abs(x)) + ')'
    else:
        return 'exp(i*pi/' + str(x) + ')'