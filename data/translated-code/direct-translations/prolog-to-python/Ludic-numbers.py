```python
# John Devou: 26-Nov-2021

def d(_, _, [], []):
    return

def d(N, N, Xs, Rs):
    d(N, 1, Xs, Rs)

def d(N, M, Xs, Rs):
    if not Xs:
        return Rs
    else:
        if M < N:
            Rs.append(Xs[0])
            d(N, M + 1, Xs[1:], Rs)

def l(Xs):
    Rs = []
    for X in Xs:
        d(X, 1, Xs, Ys)
        Rs.append(Ys)
    return Rs

def g(N):
    L = list(range(2, N+1))
    return [1] + l(L)

def s(N, Xs):
    Ls = []
    for i in range(N):
        Ls.append(Xs[i])
    Rs = Xs[N:]
    return Ls, Rs

def t(Xs):
    if len(Xs) < 3:
        return
    else:
        if Xs[1] == Xs[0] + 2 and Xs[2] == Xs[0] + 6:
            return Xs[:3]
        else:
            return t(Xs[1:])

# tasks

def t1():
    L = g(500)
    X, _ = s(25, L)
    print(X)

def t2():
    L = g(1000)
    X = len(L)
    print(X)

def t3():
    L = g(22000)
    _, R = s(1999, L)
    X, _ = s(6, R)
    print(X)

def t4():
    L = g(249)
    X = [t(L) for _ in range(len(L))]
    print(X)
```