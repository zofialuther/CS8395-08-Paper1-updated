def getSequence(rlistSize, slistSize):
    rlist = []
    slist = []
    rlist.extend([1, 3, 7])
    slist.extend([2, 4, 5, 6])
    list = rlist if rlistSize > 0 else slist
    targetSize = rlistSize if rlistSize > 0 else slistSize
    while len(list) > targetSize:
        list.pop()
    while len(list) < targetSize:
        lastIndex = len(rlist) - 1
        lastr = rlist[lastIndex]
        r = lastr + slist[lastIndex]
        rlist.append(r)
        for s in range(lastr + 1, r + 1):
            if s < r and len(list) < targetSize:
                slist.append(s)
    return list

def ffr(n):
    return getSequence(n, 0)[n - 1]

def ffs(n):
    return getSequence(0, n)[n - 1]

def main(args):
    print("R():")
    for n in range(1, 11):
        print(ffr(n))
    first40R = set()
    for n in range(1, 41):
        first40R.add(ffr(n))
    first960S = set()
    for n in range(1, 961):
        first960S.add(ffs(n))
    for i in range(1, 1001):
        n = i
        if (n in first40R) == (n in first960S):
            print("Integer " + str(i) + " either in both or neither set")
    print("Done")