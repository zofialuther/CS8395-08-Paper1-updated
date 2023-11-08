class PermutationGenerator:
    def __init__(self, n, firstNum_):
        if n < 1:
            raise ValueError("The n must be min. 1")
        self.firstNum = firstNum_
        self.array = list(range(firstNum_, n + firstNum_))
        self.firstReady = False

    def reset(self):
        self.array = list(range(self.firstNum, len(self.array) + self.firstNum))
        self.firstReady = False

    def hasMore(self):
        end = self.firstReady
        for i in range(1, len(self.array)):
            end = end and self.array[i] < self.array[i-1]
        return not end

    def getNext(self):
        if not self.firstReady:
            self.firstReady = True
            return self.array

        j = len(self.array) - 2
        k = len(self.array) - 1

        while self.array[j] > self.array[j+1]:
            j -= 1

        while self.array[j] > self.array[k]:
            k -= 1

        self.array[k], self.array[j] = self.array[j], self.array[k]

        r = len(self.array) - 1
        s = j + 1

        while r > s:
            self.array[s], self.array[r] = self.array[r], self.array[s]
            s += 1
            r -= 1

        return self.array

# For testing of the PermutationGenerator class
pg = PermutationGenerator(3, 1)

while pg.hasMore():
    temp = pg.getNext()
    for i in range(len(temp)):
        print(temp[i], end=" ")
    print()