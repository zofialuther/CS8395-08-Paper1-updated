def eulerSopConjecture():
    MAX_NUMBER = 250
    found = False
    fifth = [0] * MAX_NUMBER

    for i in range(1, MAX_NUMBER+1):
        i2 = i * i
        fifth[i - 1] = i2 * i2 * i

    for a in range(0, MAX_NUMBER+1):
        for b in range(a, MAX_NUMBER+1):
            for c in range(b, MAX_NUMBER+1):
                for d in range(c, MAX_NUMBER+1):
                    _sum = fifth[a] + fifth[b] + fifth[c] + fifth[d]
                    e = fifth.index(_sum) if _sum in fifth else -1
                    found = (e >= 0)
                    if found:
                        print(str(a+1) + "^5 + " + str(b+1) + "^5 + " + str(c+1) + "^5 + " + str(d+1) + "^5 = " + str(e+1) + "^5")