class PermutationGenerator:
    def __init__(self, n, firstNum_):
        if n < 1:
            raise ValueError("The n must be min. 1")
        self.firstNum = firstNum_
        self.array = [0] * n
        self.reset()

    def reset(self):
        for i in range(len(self.array)):
            self.array[i] = i + self.firstNum
        self.firstReady = False

    def hasMore(self):
        end = self.firstReady
        for i in range(1, len(self.array)):
            end = end and self.array[i] < self.array[i - 1]
        return not end

    def getNext(self):
        if not self.firstReady:
            self.firstReady = True
            return self.array
        temp = 0
        j = len(self.array) - 2
        k = len(self.array) - 1
        while self.array[j] > self.array[j + 1]:
            j -= 1
        while self.array[j] > self.array[k]:
            k -= 1
        temp = self.array[k]
        self.array[k] = self.array[j]
        self.array[j] = temp
        r = len(self.array) - 1
        s = j + 1
        while r > s:
            temp = self.array[s]
            self.array[s] = self.array[r]
            self.array[r] = temp
            s += 1
            r -= 1
        return self.array

    def main(self, args):
        pg = PermutationGenerator(3, 1)
        while pg.hasMore():
            temp = pg.getNext()
            for i in range(len(temp)):
                print(temp[i], end=" ")
            print("\n")