class MertensFunction:
    def main(self):
        print("First 199 terms of the merten function are as follows:")
        for n in range(1, 200):
            print(self.mertenFunction(n), end="  ")
            if (n+1) % 20 == 0:
                print()

        for exponent in range(3, 9):
            zeroCount = 0
            zeroCrossingCount = 0
            positiveCount = 0
            negativeCount = 0
            mSum = 0
            mMin = float('inf')
            mMinIndex = 0
            mMax = float('-inf')
            mMaxIndex = 0
            nMax = 10**exponent
            for n in range(1, nMax+1):
                m = self.mertenFunction(n)
                mSum += m
                if m < mMin:
                    mMin = m
                    mMinIndex = n
                if m > mMax:
                    mMax = m
                    mMaxIndex = n
                if m > 0:
                    positiveCount += 1
                if m < 0:
                    negativeCount += 1
                if m == 0:
                    zeroCount += 1
                if m == 0 and self.mertenFunction(n - 1) != 0:
                    zeroCrossingCount += 1
            print("For M(x) with x from 1 to " + str(nMax))
            print("The maximum of M(x) is M(" + str(mMaxIndex) + ") = " + str(mMax))
            print("The minimum of M(x) is M(" + str(mMinIndex) + ") = " + str(mMin))
            print("The sum of M(x) is " + str(mSum))
            print("The count of positive M(x) is " + str(positiveCount) + ", count of negative M(x) is " + str(negativeCount))
            print("M(x) has " + str(zeroCount) + " zeroes in the interval.")
            print("M(x) has " + str(zeroCrossingCount) + " crossings in the interval.")

    MU_MAX = 100000000
    MU = None
    MERTEN = None

    def mertenFunction(self, n):
        if self.MERTEN is not None:
            return self.MERTEN[n]

        self.MU = [1] * (self.MU_MAX + 1)
        self.MERTEN = [0] * (self.MU_MAX + 1)
        self.MERTEN[1] = 1
        sqrt = int(self.MU_MAX ** 0.5)

        for i in range(2, sqrt + 1):
            if self.MU[i] == 1:
                for j in range(i, self.MU_MAX + 1, i):
                    self.MU[j] *= -i
                for j in range(i*i, self.MU_MAX + 1, i*i):
                    self.MU[j] = 0

        mSum = 1
        for i in range(2, self.MU_MAX + 1):
            if self.MU[i] == i:
                self.MU[i] = 1
            elif self.MU[i] == -i:
                self.MU[i] = -1
            elif self.MU[i] < 0:
                self.MU[i] = 1
            elif self.MU[i] > 0:
                self.MU[i] = -1
            mSum += self.MU[i]
            self.MERTEN[i] = mSum
        return self.MERTEN[n]