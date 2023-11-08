```python
def btmult(A, B, C):
    multiplication(B, C, A)

def neg(A, B):
    B = list(map(lambda x: opp(x), A))

def opp(x):
    if x == 48:
        return 48
    elif x == 45:
        return 43
    elif x == 43:
        return 45

def multiplication(BIn, QIn, AOut):
    B = list(BIn)
    Q = list(QIn)
    if B[0] == 45:
        Pos0 = False
        neg(B, BP)
    else:
        BP = B
        Pos0 = True
    
    if Q[0] == 45:
        neg(Q, QP)
        Pos1 = Pos0
    else:
        QP = Q
        Pos1 = Pos0
    
    A = multiplication_(BP, QP, [48])
    
    if Pos1 == False:
        neg(A, A1)
    else:
        A1 = A
    
    AOut = A1

def multiplication_(B, T, A, AF):
    if len(T) == 0:
        return A
    else:
        H = T[0]
        B1 = multiplication_1(B, H)
        A1 = A + [48]
        A2 = bt_add1(B1, A1)
        multiplication_(B, T[1:], A2, AF)

def multiplication_1(B, H):
    if H == 43:
        return B
    elif H == 48:
        return [48]
    elif H == 45:
        return neg(B)

def division(AIn, BIn, QOut, ROut):
    A = list(AIn)
    B = list(BIn)
    LB = len(B)
    LA = len(A)
    Len = LA - LB
    
    if Len < 0:
        Q = [48]
        R = A
    else:
        NegB = neg(B)
        division_(A, B, NegB, LB, Len, [], Q, R)
    
    QOut = Q
    ROut = R

def division_(A, B, NegB, LenB, LenA, QC, QF, R):
    if LenA == -1:
        if A[0] == 45:
            positive(A, B, QC, QF, R)
        else:
            QF = QC
            R = A
    else:
        Len = LenA
        AR = A[:Len]
        AF = A[Len:]
        LR = len(AR)
        if LR >= LenB:
            if AR[0] == 43:
                S = bt_add1(AR, NegB)
                Q0 = [43]
                if len(S) == LenB and S[0] == 43:
                    S1 = bt_add1(S, NegB)
                    QC1 = bt_add1(QC, [43])
                    Q00 = [45]
                else:
                    S1 = S
                    QC1 = QC
                    Q00 = Q0
            else:
                S1 = bt_add1(AR, B)
                Q00 = [45]
                QC1 = QC
            Q1 = QC1 + Q00
            A1 = S1 + AF
            A2 = strip_nombre(A1, [])
            LenA1 = LenA - 1
            division_(A2, B, NegB, LenB, LenA1, Q1, QF, R)
        else:
            Q1 = QC + [48]
            LenA1 = LenA - 1
            division_(A, B, NegB, LenB, LenA1, Q1, QF, R)

def extract(Len, A, AR1, AF1):
    if Len == 0:
        AR1 = []
        AF1 = []
    else:
        H = A[0]
        T = A[1:]
        N = Len - 1
        if N > 0:
            AR1 = [H] + AR
            AF1 = AF
        else:
            AR1 = AR
            AF1 = [H] + AF

def positive(R, _, Q, QF, R):
    if R[0] == 43:
        positive(R, B, Q1, QF, R)
    else:
        QF = Q
        R = R

def euclide(A, B, Q, R):
    mult(A, B, Q, R)

def mult(AIn, BIn, QIn, RIn):
    if AIn:
        A = list(AIn)
    else:
        A = AIn
    
    if BIn:
        B = list(BIn)
    else:
        B = BIn
    
    if QIn:
        Q = list(QIn)
    else:
        Q = QIn
    
    if RIn:
        R = list(RIn)
    else:
        R = RIn
    
    if B[0] == 45:
        Pos0 = False
        neg(B, BP)
    else:
        BP = B
        Pos0 = True
    
    if Q and Q[0] == 45:
        neg(Q, QP)
        Pos1 = Pos0
    elif Q:
        QP = Q
        Pos1 = Pos0
    else:
        Pos1 = Pos0
    
    if A and A[0] == 45:
        neg(A, AP)
    elif A:
        AP = A
    else:
        AP = A
    
    if R:
        R1 = R
    else:
        R1 = R
    
    if Q:
        BC = BP
        Ajout = [45]
        if R:
            bt_add1(BC, R, AP)
        else:
            AP = BC
    else:
        neg(BP, BC)
        Ajout = [43]
        QP = [48]
    
    mult_(BC, QP, AP, R1, Resultat, Ajout)
    
    if not Q:
        if Pos1 == False:
            neg(Resultat, QT)
        else:
            QT = Resultat
        Q = QT
    
    if not A:
        if Pos1 == False:
            neg(Resultat, AT)
        else:
            AT = Resultat
        A = AT
    
    if not R:
        R = R1

def mult_(B, Q, A, R, Resultat, Ajout):
    Q1 = bt_add1(Q, Ajout)
    A1 = bt_add1(A, B)
    if Q1 == [48]:
        Resultat = A
    elif A1[0] == 45 and Ajout == [43]:
        Resultat = Q
        R = A
    else:
        mult_(B, Q1, A1, R, Resultat, Ajout)
```