def factors(N, Flist):
    factors(N, 2, 0, Flist)

def factors(1, _, _, []):
    return
def factors(_, _, Cnt, []):
    if Cnt > 1:
        return
    factors(N, Start, Cnt, [Fac|FList]):
        N1 = floor(sqrt(N))
        for Fac in range(Start, N1+1):
            if N % Fac == 0:
                N2 = N // Fac
                Cnt1 = Cnt + 1
                factors(N2, Fac, Cnt1, FList)
        if N >= 2:
            Flist.append(N)

def brilliantList(Start, Limit, List):
    findall N where brilliants(Start, Limit, N) into List

def nextBrilliant(Start, N):
    brilliants(Start, float('inf'), N)

def isBrilliant(N):
    brilliants(2, float('inf'), N)

def brilliants(Start, Limit, N):
    for N in range(Start, Limit+1):
        if factors(N, [F1, F2]) and F1 * F2 == N:
            D1 = digits(F1)
            D2 = digits(F2)
            if D1 == D2:
                return N

def digits(N, D):
    D = 1 + floor(log10(N))

def run(LimitList):
    run(LimitList, 0, 2)

def run([], _, _):
    return

def run([Limit|LList], OldCount, OldLimit):
    Limit1 = Limit - 1
    statistics(runtime, [Start|_])
    brilliantList(OldLimit, Limit1, BList)
    Cnt = len(BList)
    Cnt1 = OldCount + Cnt
    Index = Cnt1 + 1
    nextBrilliant(Limit, Bril)
    statistics(runtime, [Stop|_])
    Time = Stop - Start
    writef('first >=%8r is%8r at position%6r [time:%6r]', [Limit, Bril, Index, Time])
    run(LList, Cnt1, Limit)

def showList(List, Limit):
    findnsols(Limit, X, (member(X, List), writef('%5r', [X])), _)
    return

def do():
    findnsols(100, B, isBrilliant(B), BList)
    showList(BList, 10)
    LimitList = findall N where (between(1, 6, X), N is 10**X)
    run(LimitList)