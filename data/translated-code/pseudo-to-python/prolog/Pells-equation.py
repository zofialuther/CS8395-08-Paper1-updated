```python
import math

def revtl(A, Bs, Z):
    if len(A) == 0:
        Z = Bs
    else:
        revtl(A[1:], [A[0]] + Bs, Z)

def next_convergent(P0, Q0, P1, Q1, Ts, R):
    Term = Ts[0]
    P2 = Term * P1 + P0
    Q2 = Term * Q1 + Q0
    R = P1 / Q1

def convergents(A0, As, Lz):
    next_convergent(1, 0, A0, 1, As, Lz)

def cf_sqrt(N, Sz, A0, Frac):
    A0 = math.floor(math.sqrt(N))
    if A0 * A0 == N:
        Sz = 0
        Frac = []
    else:
        cf_sqrt_helper(N, A0, A0, 0, 1, 0, [], Sz, Frac)

def cf_sqrt_helper(N, A, A0, M0, D0, Sz0, L, Sz, R):
    M1 = D0 * A0 - M0
    D1 = math.floor((N - M1 * M1) / D0)
    A1 = math.floor((A + M1) / D1)
    if A1 == 2 * A:
        Sz = Sz0 + 1
        R = revtl([A1] + L, [], R)
    else:
        Sz1 = Sz0 + 1
        cf_sqrt(N, A, A1, M1, D1, Sz1, [A1] + L, Sz, R)

def pell(N, X, Y):
    cf_sqrt(N, _, D)
    convergents(D, Rs)
    found = False
    for R in Rs:
        P, Q = ratio(R)
        if P * P - N * Q * Q == 1:
            found = True
            break
    if found:
        pell_seq(N, P, Q, X, Y)

def ratio(N):
    if isinstance(N, int):
        return [N, 1]
    else:
        return N.split('/')

def pell_seq(N, X0, Y0, X2, Y2):
    pell_seq(N, X0, Y0, X1, Y1)
    X2 = X0 * X1 + N * Y0 * Y1
    Y2 = X0 * Y1 + Y0 * X1
```