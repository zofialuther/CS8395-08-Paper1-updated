```python
def continued_fraction():
    continued_fraction(200, sqrt_2_ab, V1)
    print("sqrt(2) = " + str(V1))

    continued_fraction(200, napier_ab, V2)
    print("e       = " + str(V2))

    continued_fraction(200, pi_ab, V3)
    print("pi      = " + str(V3))

def continued_fraction(N, Compute_ab, V):
    continued_fraction(N, Compute_ab, 0, V)

def continued_fraction(0, Compute_ab, Temp, V):
    Compute_ab(0, A, _)
    V = A + Temp

def continued_fraction(N, Compute_ab, Tmp, V):
    Compute_ab(N, A, B)
    Tmp1 = B / (A + Tmp)
    N1 = N - 1
    continued_fraction(N1, Compute_ab, Tmp1, V)

def sqrt_2_ab(0, 1, 1)
def sqrt_2_ab(_, 2, 1)

def napier_ab(0, 2, _)
def napier_ab(1, 1, 1)
def napier_ab(N, N, V):
    V = N - 1

def pi_ab(0, 3, _)
def pi_ab(N, 6, V):
    V = (2 * N - 1)*(2 * N - 1)
```