import lambda

def fib(N, F):
    if N < 0:
        print('fib is undefined for negative numbers.')
        return
    else:
        PF = lambda Nb, R, Rr1: R if Nb < 2 else (N1 := Nb - 1, N2 := Nb - 2, Rr1(N1, R1, Rr1), Rr1(N2, R2, Rr1), R := R1 + R2)
        Pred = PF + lambda Nb2, F2: call(PF, Nb2, F2, PF)
        call(Pred, N, F)