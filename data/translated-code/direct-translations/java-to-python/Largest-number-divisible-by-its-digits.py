class LynchBell:

    s = ""

    @staticmethod
    def main(args):
        # Highest number with unique digits (no 0 or 5)
        i = 98764321
        isUnique = True
        canBeDivided = True
        while i > 0:
            LynchBell.s = str(i)
            isUnique = LynchBell.uniqueDigits(i)
            if isUnique:
                # Number has unique digits
                canBeDivided = LynchBell.testNumber(i)
                if canBeDivided:
                    print("Number found: " + str(i))
                    i = 0
            i -= 1

    @staticmethod
    def uniqueDigits(i):
        # returns true, if unique digits, false otherwise
        for k in range(len(LynchBell.s)):
            for l in range(k + 1, len(LynchBell.s)):
                if LynchBell.s[l] == '0' or LynchBell.s[l] == '5':
                    # 0 or 5 is a digit
                    return False
                if LynchBell.s[k] == LynchBell.s[l]:
                    # non-unique digit
                    return False
        return True

    @staticmethod
    def testNumber(i):
        # Tests, if i is divisible by all its digits (0 is not a digit already)
        j = 0
        divisible = True
        for ch in LynchBell.s:
            j = int(ch)
            divisible = (i % j) == 0
            if not divisible:
                return False
        return True