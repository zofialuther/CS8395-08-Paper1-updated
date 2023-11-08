class GameNumber(AbstractGuessNumber):

    def __init__(self):
        super().__init__(4)
        self.defineNumber()

    def isGuess(self, digits):
        return (digits is not None and self.isUnique(digits) and self.isAllDigits(digits))

    def isAllDigits(self, array):
        for i in range(len(array)):
            digit = chr(array[i] + ord('0'))
            if not digit.isdigit():
                return False
        return True

    def isUnique(self, array):
        for j in range(len(array)):
            a = array[j]
            for i in range(j):
                if a == array[i]:
                    return False
        return True

    def parseDigits(self, number, length):
        arr = [0] * length
        temp = number
        for i in range(length - 1, -1, -1):
            arr[i] = temp % 10
            temp //= 10
        return arr

    def defineNumber(self):
        arr = self.generateRandom()
        for i in range(self.getLength()):
            self.digits[i] = arr[i]

    def generateRandom(self):
        while True:
            random = Random()
            number = random.randint(123, 9876)
            arr = self.parseDigits(number, self.getLength())
            if self.isGuess(arr):
                return arr

    def __str__(self):
        return str(self.digits)