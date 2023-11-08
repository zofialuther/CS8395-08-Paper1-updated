```python
class GameNumber(AbstractGuessNumber):
    def checkValidGuess(self, guess):
        # method for checking if a given array of digits is a valid guess
        pass

    def parseNumber(self, number):
        # method for parsing a number into an array of digits
        pass

    def generateRandom(self):
        # method for generating a random 4-digit number for the game
        pass

    def defineNumber(self):
        # method for initializing the game's number
        self.generateRandom()
        self.digits = []

    def toString(self):
        # method for returning the digits array as a string
        return ''.join(map(str, self.digits))
```