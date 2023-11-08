import random

class BullsAndCows:
    def main(self):
        gen = random.Random()
        target = gen.randint(1000, 9999)
        targetStr = str(target)
        guessed = False
        guesses = 0
        while not guessed:
            bulls = 0
            cows = 0
            guess = int(input("Enter a 4-digit number: "))
            try:
                guesses += 1
                guessStr = str(guess)
                for i in range(4):
                    if guessStr[i] == targetStr[i]:
                        bulls += 1
                    elif guessStr[i] in targetStr:
                        cows += 1
                if bulls == 4:
                    guessed = True
                else:
                    print("Bulls:", bulls, "Cows:", cows)
            except:
                continue
        print("Number of guesses:", guesses)

    def hasDupes(self, number):
        digs = [False] * 10
        while number > 0:
            digit = number % 10
            if digs[digit]:
                return True
            digs[digit] = True
            number = number // 10
        return False