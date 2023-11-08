def properDivsSum(n):
    sum = 0
    for i in range(1, (n + 1) // 2 + 1):
        if n % i == 0 and n != i:
            sum = sum + i
    return sum

def aliquot(n, maxLen, maxTerm):
    s = []
    s.append(n)
    newN = n
    while len(s) <= maxLen and newN < maxTerm:
        newN = properDivsSum(s[len(s) - 1])
        if newN in s:
            if s[0] == newN:
                if len(s) == 1:
                    return report("Perfect", s)
                elif len(s) == 2:
                    return report("Amicable", s)
                else:
                    return report("Sociable of length " + str(len(s)), s)
            elif s[len(s) - 1] == newN:
                return report("Aspiring", s)
            else:
                return report("Cyclic back to " + str(newN), s)
        else:
            s.append(newN)
            if newN == 0:
                return report("Terminating", s)
    return report("Non-terminating", s)

def report(msg, result):
    print(msg + ": " + str(result))
    return False

def main():
    arr = [11, 12, 28, 496, 220, 1184, 12496, 1264460, 790, 909, 562, 1064, 1488]
    for n in range(1, 11):
        aliquot(n, 16, 1 << 47)
    for n in arr:
        aliquot(n, 16, 1 << 47)