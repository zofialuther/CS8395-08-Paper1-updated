def fib(N, F):
    if N < 0:
        print("fib is undefined for negative numbers.")
    else:
        def PF(Nb, R, Rr1):
            if Nb < 2:
                R = Nb
            else:
                N1 = Nb - 1
                N2 = Nb - 2
                call(Rr1, N1, R1, Rr1)
                call(Rr1, N2, R2, Rr1)
                R = R1 + R2
        
        def Pred(Nb2, F2):
            call(PF, Nb2, F2, PF)
        
        call(Pred, N, F)