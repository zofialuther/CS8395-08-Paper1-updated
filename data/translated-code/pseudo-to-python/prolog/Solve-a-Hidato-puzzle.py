from pyswip import Prolog

prolog = Prolog()
prolog.consult('clpfd.pl')

def hidato():
    init1(Li)
    init2(1, 1, 10, Li)
    my_write(Li)

def init1(Li):
    Li = [0] * 100
    LV = [x for x in Li if 1 <= x <= 40]
    LV = list(set(LV))
    for i in range(len(LV)):
        LV[i] in LV
    return

def init2(_N, Col, Max_Col, _L):
    if Col == Max_Col - 1:
        return
    if _L[_N] == 0:
        return
    if Col == 1:
        return
    if Col == Max_Col:
        return
    else:
        compute_BI(_L, V, I, VI, BI)
        # update values of N, Lig, and Col

def compute_BI(L, V, I, VI, BI):
    VI = L[I]
    if VI == 0:
        BI = 0
    else:
        BI = 1 if abs(V - VI) == 1 else -1
    return

def my_write([0, A, B, C, D, E, F, G, H, 0 | T]):
    print(A, B, C, D, E, F, G, H)
    my_write(T)

def my_write([]):
    return

def my_write_1(0):
    print("   ")

def my_write_1(X):
    print(X)

# This is just a translation of the pseudocode to Python, so it may not be fully functional.