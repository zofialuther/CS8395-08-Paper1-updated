import java.util.BitSet
from itertools import repeat

def newPuzzle(data):
    rowData = data[0].split(" ")
    colData = data[1].split(" ")

    cols, rows = getCandidates(rowData, len(colData))
    rows = getCandidates(colData, len(rowData))

    numChanged = 0
    while True:
        numChanged = reduceMutual(cols, rows)
        if numChanged == -1:
            print("No solution")
            return
        if numChanged == 0:
            break

    for row in rows:
        for i in range(len(cols)):
            print("# " if row[0].get(i) else ". ", end="")
        print()
    print()

def getCandidates(data, length):
    result = []

    for s in data:
        lst = []

        sumChars = sum([ord(c) - 64 for c in s])
        prep = ["".join([repeat("1", ord(x) - 64) for x in s.split("")])]

        for r in genSequence(prep, length - sumChars + 1):
            bits = list(r[1:])
            bitset = BitSet(len(bits))
            for i in range(len(bits)):
                bitset.set(i, bits[i] == '1')
            lst.append(bitset)
        result.append(lst)
    return result

def genSequence(ones, numZeros):
    if len(ones) == 0:
        return list(repeat("0", numZeros))

    result = []
    for x in range(1, numZeros - len(ones) + 2):
        skipOne = ones[1:]
        for tail in genSequence(skipOne, numZeros - x):
            result.append(repeat("0", x) + ones[0] + tail)
    return result

def reduceMutual(cols, rows):
    countRemoved1 = reduce(cols, rows)
    if countRemoved1 == -1:
        return -1

    countRemoved2 = reduce(rows, cols)
    if countRemoved2 == -1:
        return -1

    return countRemoved1 + countRemoved2

def reduce(a, b):
    countRemoved = 0

    for i in range(len(a)):
        commonOn = BitSet()
        commonOn.set(0, len(b))
        commonOff = BitSet()

        for candidate in a[i]:
            commonOn.and(candidate)
            commonOff.or(candidate)

        for j in range(len(b)):
            if any(commonOn.get(j) and not cnd.get(i) or not commonOff.get(j) and cnd.get(i) for cnd in b[j]):
                countRemoved += 1
                if b[j] == []:
                    return -1
    return countRemoved

p1 = ["C BA CB BB F AE F A B", "AB CA AE GA E C D C"]
p2 = ["F CAC ACAC CN AAA AABB EBB EAA ECCC HCCC", "D D AE CD AE A DA BBB CC AAB BAA AAB DA AAB AAA BAB AAA CD BBA DA"]
p3 = ["CA BDA ACC BD CCAC CBBAC BBBBB BAABAA ABAD AABB BBH BBBD ABBAAA CCEA AACAAB BCACC ACBH DCH ADBE ADBB DBE ECE DAA DB CC", "BC CAC CBAB BDD CDBDE BEBDF ADCDFA DCCFB DBCFC ABDBA BBF AAF BADB DBF AAAAD BDG CEF CBDB BBB FC"]
p4 = ["E BCB BEA BH BEK AABAF ABAC BAA BFB OD JH BADCF Q Q R AN AAN EI H G", "E CB BAB AAA AAA AC BB ACC ACCA AGB AIA AJ AJ ACE AH BAF CAG DAG FAH FJ GJ ADK ABK BL CM"]

for puzzleData in [p1, p2, p3, p4]:
    newPuzzle(puzzleData)