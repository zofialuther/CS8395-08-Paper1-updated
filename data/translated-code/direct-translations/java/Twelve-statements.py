class LogicPuzzle:
    def __init__(self):
        self.S = [False]*13
        self.Count = 0

    def check2(self):
        count = 0
        for k in range(7, 13):
            if self.S[k]:
                count += 1
        return self.S[2] == (count == 3)

    def check3(self):
        count = 0
        for k in range(2, 13, 2):
            if self.S[k]:
                count += 1
        return self.S[3] == (count == 2)

    def check4(self):
        return self.S[4] == (not self.S[5] or (self.S[6] and self.S[7]))

    def check5(self):
        return self.S[5] == (not self.S[2] and not self.S[3] and not self.S[4])

    def check6(self):
        count = 0
        for k in range(1, 12, 2):
            if self.S[k]:
                count += 1
        return self.S[6] == (count == 4)

    def check7(self):
        return self.S[7] == ((self.S[2] or self.S[3]) and not (self.S[2] and self.S[3]))

    def check8(self):
        return self.S[8] == (not self.S[7] or (self.S[5] and self.S[6]))

    def check9(self):
        count = 0
        for k in range(1, 7):
            if self.S[k]:
                count += 1
        return self.S[9] == (count == 3)

    def check10(self):
        return self.S[10] == (self.S[11] and self.S[12])

    def check11(self):
        count = 0
        for k in range(7, 10):
            if self.S[k]:
                count += 1
        return self.S[11] == (count == 1)

    def check12(self):
        count = 0
        for k in range(1, 12):
            if self.S[k]:
                count += 1
        return self.S[12] == (count == 4)

    def check(self):
        if (self.check2() and self.check3() and self.check4() and self.check5() and self.check6()
            and self.check7() and self.check8() and self.check9() and self.check10() and self.check11()
            and self.check12()):
            for k in range(1, 13):
                if self.S[k]:
                    print(k, end=" ")
            print()
            self.Count += 1

    def recurseAll(self, k):
        if k == 13:
            self.check()
        else:
            self.S[k] = False
            self.recurseAll(k + 1)
            self.S[k] = True
            self.recurseAll(k + 1)

    def main(self):
        P = LogicPuzzle()
        P.S[1] = True
        P.recurseAll(2)
        print()
        print(P.Count, "Solutions found.")

# Run the main method
P = LogicPuzzle()
P.main()