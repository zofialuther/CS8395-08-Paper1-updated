```python
from math import floor, sqrt, log10

def factors(N, Flist):
    factors_helper(N, 2, 0, Flist)

def factors_helper(N, Start, Cnt, Flist):
    if N == 1:
        return
    if Cnt > 1:
        return
    N1 = floor(sqrt(N))
    for Fac in range(Start, N1 + 1):
        if N % Fac == 0:
            N2 = N // Fac
            Cnt1 = Cnt + 1
            factors_helper(N2, Fac, Cnt1, Flist)
            Flist.append(Fac)
            return
    if N >= 2:
        Flist.append(N)

def brilliantList(Start, Limit):
    return [N for N in range(Start, Limit) if isBrilliant(N)]

def nextBrilliant(Start):
    N = Start
    while True:
        if isBrilliant(N):
            return N
        N += 1

def isBrilliant(N):
    Flist = []
    factors(N, Flist)
    if len(Flist) != 2:
        return False
    F1, F2 = Flist
    if F1 * F2 != N:
        return False
    if len(str(F1)) != len(str(F2)):
        return False
    return True

def digits(N):
    return 1 + floor(log10(N))

def run(LimitList, OldCount, OldLimit):
    if not LimitList:
        return
    Limit = LimitList[0]
    Limit1 = Limit - 1
    BList = brilliantList(OldLimit, Limit1)
    Cnt = len(BList)
    Cnt1 = OldCount + Cnt
    Index = Cnt1 + 1
    Bril = nextBrilliant(Limit)
    print(f'first >= {Limit} is {Bril} at position {Index}')
    LimitList.pop(0)
    run(LimitList, Cnt1, Limit)

def showList(List, Limit):
    for item in List:
        print(f'{item}', end=' ')
    print()

def do():
    BList = [N for N in range(1, 10**6) if isBrilliant(N)]
    showList(BList[:100], 10)
    LimitList = [10**X for X in range(1, 7)]
    run(LimitList, 0, 2)

do()
```