```python
def wheel2357(L):
    W = [2,  4,  2,  4,  6,  2,  6,  4,
         2,  4,  6,  6,  2,  6,  4,  2,
         6,  4,  6,  8,  4,  2,  4,  2,
         4,  8,  6,  4,  6,  2,  4,  6,
         2,  6,  6,  4,  2,  4,  6,  2,
         6,  4,  2,  4,  2, 10,  2, 10]
    L = [1, 2, 2, 4]
    L.extend(W)

def factor(N, Fac):
    if N == 1:
        return 1
    else:
        wheel2357(W)
        return factor(N, 2, W, 1, Fac0)

def factor(N, F, W, Fac1, Fac2):
    if F*F > N:
        return add_factor(N, Fac1, Fac2)
    elif N > 1:
        divmod(N, F, Q, 0)
        add_factor(F, Fac1, Fac2)
        return factor(Q, F, W, Fac2, Fac)
    else:
        F2 = F + W[0]
        return factor(N, F2, W[1:], Fac1, Fac)

def add_factor(F, Fac):
    if F == 1:
        return F
    elif F == F:
        return F**2
    else:
        return F*Fac

def reverse_factors(A, B):
    return reverse_factors(B, C), A*B
```