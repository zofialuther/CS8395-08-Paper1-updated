def divisor(N, Divisor):
    UpperBound = round(sqrt(N))
    for D in range(1, UpperBound+1):
        if N % D == 0:
            Divisor = D
        else:
            LargerDivisor = N / D
            if LargerDivisor != D:
                Divisor = LargerDivisor

def proper_divisor(N, D):
    divisor(N, D)
    if D != N:
        return True
    else:
        return False

def assoc_num_divsSum_in_range(Low, High, Assoc):
    Pairs = []
    for Num in range(Low, High+1):
        DivSum = 0
        for D in range(1, Num):
            if proper_divisor(Num, D):
                DivSum = DivSum + D
        Pairs.append((Num-DivSum))
    Assoc = dict(Pairs)

def get_amicable_pair(Assoc, M):
    N = Assoc[M]
    if M < N:
        return (M-N)

def amicable_pairs_under_20000():
    Pairs = []
    Assoc = assoc_num_divsSum_in_range(1, 20000)
    for M in range(1, 20001):
        P = get_amicable_pair(Assoc, M)
        if P:
            Pairs.append(P)
    return Pairs