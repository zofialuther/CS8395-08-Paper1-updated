def LynchBell():
    s = ""
    i = 98764321
    isUnique = True
    canBeDivided = True
    while i > 0:
        s = str(i)
        isUnique = uniqueDigits(s)
        if isUnique:
            canBeDivided = testNumber(s, i)
            if canBeDivided:
                print("Number found: " + str(i))
                i = 0
        i = i - 1

def uniqueDigits(s):
    for k in range(len(s)):
        for l in range(k + 1, len(s)):
            if s[l] == '0' or s[l] == '5':
                return False
            if s[k] == s[l]:
                return False
    return True

def testNumber(s, i):
    j = 0
    divisible = True
    for ch in s:
        j = int(ch)
        divisible = (i % j) == 0
        if not divisible:
            return False
    return True