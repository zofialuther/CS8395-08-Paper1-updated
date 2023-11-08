```python
from itertools import combinations

def digits(N, DList):
    if N == 0:
        return
    else:
        D, N1 = divmod(N, 10)
        DList.append(D)
        digits(N1, DList)

def combi(N, arr, result, temp, start):
    if N == 0:
        result.append(temp[:])
        return
    for i in range(start, len(arr)):
        temp.append(arr[i])
        combi(N-1, arr, result, temp, i)
        temp.pop()

def powSum(DList, Pow, Acc):
    if len(DList) == 0:
        return Acc
    else:
        Acc1 = Acc + DList[0] ** Pow
        return powSum(DList[1:], Pow, Acc1)

def armstrong(Exp, PSum):
    DigList = list(range(10))
    if Exp > 1:
        Min = 10 ** (Exp - 1)
    else:
        Min = 0
    Max = 10 ** Exp - 1
    Comb = []
    combi(Exp, DigList, Comb, [], 0)
    for P in range(Min, Max + 1):
        DList = []
        digits(P, DList)
        DList.sort()
        if (DList == Comb) or (P == 0 and Comb == [0]):
            tempSum = powSum(DList, Exp, 0)
            if tempSum == P:
                PSum.append(P)

def main():
    for Exp in range(1, 8):
        AList = []
        armstrong(Exp, AList)
        print(f'{Exp} -> {AList}')

main()
```