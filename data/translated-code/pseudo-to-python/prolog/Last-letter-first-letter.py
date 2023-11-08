```python
def last_first(Len, Nb, L):
    retractall(res(_,_,_))
    assert(res(0, 0, []))
    last_first()
    res(Len, Nb, L1)
    maplist(lambda X, Y: X == [Y, _, _], L1, L)

def last_first():
    init(L)
    for Word in L:
        if not lance_p([Word] + L1):
            continue

def lance_p(L):
    LF = p(L)
    retract(res(Len, Nb, Lst))
    Len1 = len(LF)
    if Len1 > Len:
        assert(res(Len1, 1, LF))
    elif Len1 == Len:
        Nb1 = Nb + 1
        assert(res(Len, Nb1, Lst))
    else:
        assert(res(Len, Nb, Lst))
    return False

def p(L, L):
    if not select(B, L, L1):
        return False
    if not p0(A,B):
        return False
    T = [B] + T1
    p([B] + T1, [B] + L1)

def p(A, _):
    return True

def p0(A, B):
    return A[2] == B[1] and A[1] == B[2]

def init(L):
    L0 = [ "audino", "bagon", "baltoy", ... ] # (list of words)
    maplist(init_, L0, L)

def init_(W, FL):
    first_letter(W, F)
    last_letter(W, L)
    FL = [W, F, L]

def first_letter(A):
    FC = list(A)
    F = FC[0]

def last_letter(A):
    LC = list(A)
    RLC = LC[::-1]
    L = RLC[0]
```