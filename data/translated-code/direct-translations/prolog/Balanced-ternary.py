```python
from functools import reduce

def multiplication(BIn, QIn):
    def neg(A, B):
        return [43 if x == 45 else 45 if x == 43 else x for x in A], B

    def opp(x, y):
        return 43 if x == 45 else 45 if x == 43 else 48

    def multiplication_(B, Q, A):
        if not Q:
            return A
        else:
            H, *T = Q
            B1 = B if H == 43 else B
            A1 = A + [48]
            A2 = bt_add1(B1, A1)
            return multiplication_(B, T, A2)

    B = list(BIn)
    Q = list(QIn)

    B, Pos0 = (neg(B, []) if B[0] == 45 else (B, True))
    Q, Pos1 = (neg(Q, []) if Q[0] == 45 else (Q, Pos0))

    A = multiplication_(B, Q, [48])

    if not Pos1:
        A = neg(A, [])

    return ''.join(A)


def division(AIn, BIn):
    def extract(Len, L):
        N1 = Len
        AR1, AF1 = [], []
        for H in L:
            if N1 > 0:
                AR1.append(H)
                N1 -= 1
            else:
                AF1.append(H)
        return AR1, AF1

    def positive(R, Q):
        if R[0] == 43:
            return [43], R
        else:
            S = bt_add1(R, B)
            Q1 = bt_add1(Q, [45])
            return positive(S, Q1)

    def division_(A, B, NegB, LenB, LenA, QC):
        if LenA == -1:
            if A[0] == 45:
                return positive(A, B, QC, QC, [])
            else:
                return QC, A
        else:
            AR, AF = extract(LenA, A)
            LR = len(AR)
            if LR >= LenB:
                if AR[0] == 43:
                    S = bt_add1(AR, NegB)
                    if len(S) == LenB and S[0] == 43:
                        S = bt_add1(S, NegB)
                        QC1 = bt_add1(QC, [43])
                        Q00 = [45]
                    else:
                        QC1, S1 = QC, S
                        Q00 = [45]
                else:
                    S1 = bt_add1(AR, B)
                    Q00 = [45]
                    QC1 = QC
                Q1 = QC1 + Q00
                A1 = S1 + AF
                A2 = strip_nombre(A1, [])
                LenA1 = LenA - 1
                return division_(A2, B, NegB, LenB, LenA1, Q1)
            else:
                Q1 = QC + [48]
                LenA1 = LenA - 1
                return division_(A, B, NegB, LenB, LenA1, Q1)

    A = list(AIn)
    B = list(BIn)
    LB = len(B)
    LA = len(A)
    Len = LA - LB
    if Len < 0:
        Q = [48]
        R = A
    else:
        NegB = neg(B, [])
        Q, R = division_(A, B, NegB, LB, Len, [])
    return ''.join(Q), ''.join(R)
```