```python
import random

class GameNumber(AbstractGuessNumber):

    def __init__(self):
        super().__init__(4)
        self.defineNumber()

    @staticmethod
    def isGuess(digits):
        return (digits is not None and GameNumber.isUnique(digits) and GameNumber.isAllDigits(digits))

    @staticmethod
    def isAllDigits(array):
        for i in range(len(array)):
            digit = chr(array[i] + ord('0'))
            if not digit.isdigit():
                return False
        return True

    @staticmethod
    def isUnique(array):
        for j in range(len(array)):
            a = array[j]
            for i in range(j):
                if a == array[i]:
                    return False
        return True

    @staticmethod
    def parseDigits(number, length):
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
            number = random.randint(123, 9876)
            arr = GameNumber.parseDigits(number, self.getLength())
            if GameNumber.isGuess(arr):
                return arr

    def __str__(self):
        return str(self.digits)
```