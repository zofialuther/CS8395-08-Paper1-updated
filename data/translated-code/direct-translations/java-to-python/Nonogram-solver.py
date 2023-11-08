```python
from typing import List
from itertools import repeat
from collections import deque
from bitarray import bitarray

def newPuzzle(data: List[str]) -> None:
    rowData = data[0].split(" ")
    colData = data[1].split(" ")

    cols, rows = getCandidates(rowData, len(colData))
    rows, cols = getCandidates(colData, len(rowData))

    numChanged = 0
    while numChanged > 0:
        numChanged = reduceMutual(cols, rows)
        if numChanged == -1:
            print("No solution")
            return

    for row in rows:
        for i in range(len(cols)):
            print("# " if row[0][i] else ". ", end="")
        print()
    print()

def getCandidates(data: List[str], length: int) -> List[List[bitarray]]:
    result = []
    for s in data:
        lst = []

        sumChars = sum(map(lambda c: ord(c) - ord('A') + 1, s))
        prep = [repeat("1", ord(x) - ord('A') + 1) for x in s]

        for r in genSequence(prep, length - sumChars + 1):
            bits = list(r[1:])
            bitset = bitarray(bits)
            lst.append(bitset)
        result.append(lst)
    return result

def genSequence(ones: List[str], numZeros: int) -> List[str]:
    if not ones:
        return ["".join(repeat("0", numZeros))]

    result = []
    for x in range(1, numZeros - len(ones) + 2):
        skipOne = ones[1:]
        for tail in genSequence(skipOne, numZeros - x):
            result.append("".join(repeat("0", x)) + ones[0] + tail)
    return result

def reduceMutual(cols: List[List[bitarray]], rows: List[List[bitarray]]) -> int:
    countRemoved1 = reduce(cols, rows)
    if countRemoved1 == -1:
        return -1

    countRemoved2 = reduce(rows, cols)
    if countRemoved2 == -1:
        return -1

    return countRemoved1 + countRemoved2

def reduce(a: List[List[bitarray]], b: List[List[bitarray]]) -> int:
    countRemoved = 0
    for i in range(len(a)):
        commonOn = bitarray(1)
        commonOn.setall(True)
        commonOff = bitarray(1)
        commonOff.setall(False)

        for candidate in a[i]:
            commonOn &= candidate
            commonOff |= candidate

        for j in range(len(b)):
            fi = i
            fj = j

            if b[j].remove(lambda cnd: (commonOn[fj] and not cnd[fi]) or (not commonOff[fj] and cnd[fi])):
                countRemoved += 1

            if not b[j]:
                return -1
    return countRemoved
```