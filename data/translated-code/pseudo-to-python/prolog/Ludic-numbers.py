def d(N, M, Xs, Rs):
    if len(Xs) == 0:
        Rs = []
    elif N == M:
        d(N, 1, Xs, Rs)
    else:
        if M < N:
            temp = Xs.pop(0)
            Rs.append(temp)
            d(N, M + 1, Xs, Rs)

def l(Xs, Rs):
    if len(Xs) == 0:
        Rs = []
    else:
        temp = Xs.pop(0)
        Ys = []
        d(temp, 1, Xs, Ys)
        Rs.append(temp)
        l(Ys, Rs)

def g(N, X):
    L = []
    for i in range(2, N+1):
        L.append(i)
    l(L, X)
    X.insert(0, 1)

def s(N, Xs, Ls, Rs):
    if N == 0:
        Rs = Xs
    else:
        M = N - 1
        temp = Xs.pop(0)
        Ls.append(temp)
        s(M, Xs, Ls, Rs)

def t(Xs, R):
    if Xs[1] == Xs[0] + 2 and Xs[2] == Xs[0] + 6:
        R = [Xs[0], Xs[1], Xs[2]]
    else:
        temp = Xs.pop(0)
        t(Xs, R)

def t1():
    L = []
    g(500, L)
    X = []
    s(25, L, X, [])
    print(X)

def t2():
    L = []
    g(1000, L)
    X = len(L)
    print(X)

def t3():
    L = []
    g(22000, L)
    R = []
    s(1999, L, R, [])
    X = []
    s(6, R, X, [])
    print(X)

def t4():
    L = []
    g(249, L)
    X = []
    for i in range(len(L)):
        A = []
        t(L, A)
        X.append(A)
    print(X)