```python
from typing import List
from prologlib import PrologInteger, PrologList, PrologVariable, Prolog

prolog = Prolog()

prolog.assertz("proposition(4)")
prolog.assertz("digits(8)")

def tirage_1(L: PrologList) -> None:
    Len = PrologInteger(4)
    Max = Len - 1
    L = PrologList([i for i in range(Max + 1)])

def tirage(L: PrologList, Ms: PrologList) -> None:
    Len = 4
    length_Ms = len(Ms)

    Digits = 8

    Ms.in_domain(0, Digits)
    Ms.all_different()

    for i in L:
        placees(Ms, i)

    Ms.label()

def placees(Sol: PrologList, PR: PrologList) -> None:
    V = PrologInteger(0)

    BP1 = PrologVariable()
    MP1 = PrologVariable()

    BP = PR[0]
    MP = PR[1]

    compte_bien_placees(Sol, PR, V, BP1)
    BP1.unify(BP)

    compte_mal_placees(Sol, PR, PrologInteger(0), V, MP1)
    MP1.unify(MP)

def compte_mal_placees(Sol: PrologList, PR: PrologList, N: PrologInteger, MPC: PrologInteger, MPF: PrologInteger) -> None:
    if len(PR) == 0:
        MPF.unify(MPC)
    else:
        H = PR[0]
        T = PR[1:]

        VF = PrologInteger(0)
        compte_une_mal_placee(H, N, Sol, PrologInteger(0), PrologInteger(0), VF)

        MPC1 = MPC + VF
        N1 = N + 1

        compte_mal_placees(Sol, T, N1, MPC1, MPF)

def compte_une_mal_placee(H: PrologInteger, N: PrologInteger, Sol: PrologList, NH: PrologInteger, TTC: PrologInteger, TTF: PrologInteger) -> None:
    if len(Sol) == 0:
        TTF.unify(TTC)
    elif NH == N:
        NH1 = NH + 1
        compte_une_mal_placee(H, N, Sol[1:], NH1, TTC, TTF)
    elif H.value == Sol[0].value:
        NH2 = NH + 1
        TTC1 = TTC + 1
        compte_une_mal_placee(H, N, Sol[1:], NH2, TTC1, TTF)
    else:
        NH2 = NH + 1
        compte_une_mal_placee(H, N, Sol[1:], NH2, TTC, TTF)

def compte_bien_placees(Sol: PrologList, PR: PrologList, MPC: PrologInteger, MPF: PrologInteger) -> None:
    if len(PR) == 0:
        MPF.unify(MPC)
    else:
        H = PR[0]
        H1 = PR[1]

        if H.value == H1.value:
            MPC1 = MPC + 1
            compte_bien_placees(Sol[1:], PR[1:], MPC1, MPF)
        else:
            compte_bien_placees(Sol[1:], PR[1:], MPC, MPF)
```