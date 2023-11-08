```python
def continued_fraction():
    # square root 2
    V1 = continued_fraction_helper(200, sqrt_2_ab)
    print('sqrt(2) =', V1)

    # napier
    V2 = continued_fraction_helper(200, napier_ab)
    print('e       =', V2)

    # pi
    V3 = continued_fraction_helper(200, pi_ab)
    print('pi      =', V3)


# code for continued fractions
def continued_fraction_helper(N, Compute_ab):
    return continued_fraction_recursive(N, Compute_ab, 0)


def continued_fraction_recursive(N, Compute_ab, Tmp):
    if N == 0:
        return Compute_ab(0, 1, 1) + Tmp
    else:
        A, B = Compute_ab(N)
        Tmp1 = B / (A + Tmp)
        N1 = N - 1
        return continued_fraction_recursive(N1, Compute_ab, Tmp1)


# specific codes for examples
# definitions for square root of 2
def sqrt_2_ab(n):
    if n == 0:
        return 1, 1
    else:
        return 2, 1


# definitions for napier
def napier_ab(n):
    if n == 0:
        return 2, 1
    elif n == 1:
        return 1, 1
    else:
        return n, n-1


# definitions for pi
def pi_ab(n):
    if n == 0:
        return 3, 1
    else:
        return 6, (2 * n - 1) * (2 * n - 1)
```