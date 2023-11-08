def day(n, label):
    return (n, label)

def gift(n, description):
    return (n, description)

def giftsFor(N, result):
    if N == 0:
        return result
    else:
        h = gift(N, "")
        result.append(h)
        M = N - 1
        return giftsFor(M, result)

def writeln(S):
    print(S)

def writeList(arr):
    for item in arr:
        writeln(item)
    writeln('')

def writeGifts(N):
    Nth = day(N, "")
    writeln('On the ' + Nth[1] + ' day of Christmas, my true love sent to me:')
    L = []
    giftsFor(N, L)
    writeList(L)

def writeLoop(N):
    if N == 0:
        return
    else:
        Day = 13 - N
        writeGifts(Day)
        M = N - 1
        writeLoop(M)

def main():
    writeLoop(12)

main()