```python
from fractions import Fraction

def cf_sqrt(N, Sz, A0, Frac):
    A0 = int(N ** 0.5)
    if A0 * A0 == N:
        Sz = 0
        Frac = []
    else:
        cf_sqrt_recursive(N, A0, A0, 0, 1, 0, [], Sz, Frac)

def cf_sqrt_recursive(N, A, A0, M0, D0, Sz0, L, Sz, R):
    M1 = D0 * A0 - M0
    D1 = (N - M1 * M1) // D0
    A1 = (A + M1) // D1
    if A1 == 2 * A:
        Sz = Sz0 + 1
        revtl([A1] + L, R, R)
    else:
        Sz1 = Sz0 + 1
        cf_sqrt_recursive(N, A, A1, M1, D1, Sz1, [A1] + L, Sz, R)

def revtl(As, Bs, Z):
    if not As:
        Z = Bs
    else:
        revtl(As[1:], [As[0]] + Bs, Z)

def convergents(A, Lz):
    next_convergent(eval_state(1, 0, A[0], 1, A[1]), Lz)

def next_convergent(eval_state_P0, Q0, P1, Q1, Ts, R):
    P2 = Ts[0] * P1 + P0
    Q2 = Ts[0] * Q1 + Q0
    R = Fraction(P1, Q1)

def pell(N, X, Y):
    cf_sqrt(N, _, D)
    Rs = convergents(D)
    for R in Rs:
        if isinstance(R, Fraction):
            P, Q = R.numerator, R.denominator
            if P * P - N * Q * Q == 1:
                break
    pell_seq(N, P, Q, X, Y)

def ratio(N, P, Q):
    if isinstance(N, int):
        P, Q = N, 1
    else:
        P, Q = N.numerator, N.denominator

def pell_seq(N, X0, Y0, X2, Y2):
    if X0 == X2 and Y0 == Y2:
        return X0, Y0
    else:
        X1, Y1 = pell_seq(N, X0, Y0, X0 * X2 + N * Y0 * Y2, X0 * Y2 + Y0 * X2)
        return X1, Y1
```