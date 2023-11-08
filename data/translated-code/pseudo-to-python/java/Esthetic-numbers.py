def isEsthetic(n, b):
    if n == 0:
        return False
    i = n % b
    n2 = n // b
    while n2 > 0:
        j = n2 % b
        if abs(i - j) != 1:
            return False
        n2 = n2 // b
        i = j
    return True

def listEsths(n, n2, m, m2, perLine, all):
    esths = []
    def dfs(n, m, i):
        if n <= i and i <= m:
            esths.append(i)
        if i == 0 or i > m:
            return
        d = i % 10
        i1 = i * 10 + d - 1
        i2 = i1 + 2
        if d == 0:
            dfs(n, m, i2)
        elif d == 9:
            dfs(n, m, i1)
        else:
            dfs(n, m, i1)
            dfs(n, m, i2)
    for i in range(10):
        dfs(n2, m2, i)
    le = len(esths)
    print("Base 10: " + str(le) + " esthetic numbers between " + str(n) + " and " + str(m))
    if all:
        for i in range(len(esths)):
            print(esths[i])
            if (i + 1) % perLine == 0:
                print()
    else:
        for i in range(perLine):
            print(esths[i])
        print()
        print("............")
        for i in range(le - perLine, le):
            print(esths[i])
        print()

def main(args):
    for b in range(2, 17):
        print("Base " + str(b) + ": " + str(4 * b) + "th to " + str(6 * b) + "th esthetic numbers:")
        n = 1
        c = 0
        while c < 6 * b:
            if isEsthetic(n, b):
                c = c + 1
                if c >= 4 * b:
                    print(str(n))
            n = n + 1
        print()

    listEsths(1000, 1010, 9999, 9898, 16, True)
    listEsths(int(1e8), 101010101, 13 * int(1e7), 123456789, 9, True)
    listEsths(int(1e11), 101010101010, 13 * int(1e10), 123456789898, 7, False)
    listEsths(int(1e14), 101010101010101, 13 * int(1e13), 123456789898989, 5, False)
    listEsths(int(1e17), 101010101010101010, 13 * int(1e16), 123456789898989898, 4, False)