```python
def b_not(hi, lo):
    if hi:
        return False
    else:
        return True

def b_and(hi, lo):
    if hi:
        return lo
    else:
        return False

def b_or(hi, lo):
    if hi or lo:
        return True
    else:
        return False

def b_xor(A, B):
    NotA = b_not(A)
    NotB = b_not(B)
    P = b_and(A, NotB)
    Q = b_and(NotA, B)
    return b_or(P, Q)

def b_half_adder(A, B):
    S = b_xor(A, B)
    C = b_and(A, B)
    return S, C

def b_full_adder(A, B, Ci):
    S0, C0 = b_half_adder(Ci, A)
    S, C = b_half_adder(S0, B)
    C1 = b_or(C0, C)
    return S, C1

def b_4_bit_adder(A, B):
    S0, C0 = b_full_adder(A[0], B[0], False)
    S1, C1 = b_full_adder(A[1], B[1], C0)
    S2, C2 = b_full_adder(A[2], B[2], C1)
    S3, V = b_full_adder(A[3], B[3], C2)
    return S0, S1, S2, S3, V

def test_add(A, B, T):
    R = b_4_bit_adder(A, B)
    print(f'{A} + {B} is {R} \t({T})')

def go():
    test_add([True, False, False, False], [True, False, False, False], '1 + 1 = 2')
    test_add([False, True, False, False], [False, True, False, False], '2 + 2 = 4')
    test_add([True, False, True, False], [True, False, False, True], '5 + 9 = 14')
    test_add([True, True, False, True], [True, False, False, True], '11 + 9 = 20')
    test_add([False, False, False, True], [False, False, False, True], '8 + 8 = 16')
    test_add([True, True, True, True], [True, False, False, False], '15 + 1 = 16')

go()
```