from typing import Callable

def fact(N: int, FN: Callable[[int], None]) -> None:
    cont_fact(N, FN, lambda X, Y: Y = X)

def cont_fact(N: int, F: Callable[[int], None], Pred: Callable[[int, int], None]) -> None:
    if N == 0:
        Pred(1, F)
    else:
        N1 = N - 1
        P = lambda Z, T: T is Z * N
        FT = cont_fact(N1, P)
        Pred(FT, F)