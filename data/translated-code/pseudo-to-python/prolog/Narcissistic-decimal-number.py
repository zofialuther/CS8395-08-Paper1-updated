def digits(N, DList):
    if N == 0:
        return []
    else:
        N1, D = divmod(N, 10)
        digits(N1, DList)
        DList.insert(0, D)

def combi(N, lst, Comb):
    if N == 0:
        return []
    elif N > 0:
        N1 = N - 1
        combi(N1, lst, Comb)
        Comb.insert(0, lst[0])
    else:
        combi(N, lst[1:], Comb)

def powSum(DList, Pow, Acc, Sum):
    Acc1 = Acc + DList[0] ** Pow
    powSum(DList[1:], Pow, Acc1, Sum)

def armstrong(Exp, PSum):
    DigList = list(range(10))
    if Exp > 1:
        Min = 10 ** (Exp - 1)
    else:
        Min = 0
    Max = 10 ** Exp - 1
    Comb = []
    combi(Exp, DigList, Comb)
    powSum(Comb, Exp, 0, PSum)
    for PSum in range(Min, Max + 1):
        DList = []
        digits(PSum, DList)
        DList.sort()
        if DList == Comb or (PSum == 0 and Comb == [0]):
            return PSum

def do():
    for Exp in range(1, 7):
        ArmNum = armstrong(Exp, 0)
        ArmNum.sort()
        print(Exp, ArmNum)