from enum import Enum
import random

class RPS:
    class Item(Enum):
        ROCK = 0
        PAPER = 1
        SCISSORS = 2

        losesToList = {
            ROCK: [SCISSORS],
            PAPER: [ROCK],
            SCISSORS: [PAPER]
        }

        def losesTo(self, item):
            return item in self.losesToList[self]

    counts = {RPS.Item.ROCK: 1, RPS.Item.PAPER: 1, RPS.Item.SCISSORS: 1}
    totalThrows = len(RPS.Item)

    def main(self):
        rps = RPS()
        rps.run()

    def run(self):
        while True:
            user_choice = int(input("Enter your choice (0 for ROCK, 1 for PAPER, 2 for SCISSORS): "))
            if user_choice not in [0, 1, 2]:
                continue
            self.counts[RPS.Item(user_choice)] += 1
            self.totalThrows += 1
            ai_choice = self.getAIChoice()
            print("AI's choice:", ai_choice.name)
            self.determineWinner(RPS.Item(user_choice), ai_choice)

    @staticmethod
    def getAIChoice():
        choice = random.choices(list(RPS.Item), weights=[RPS.counts[item] for item in RPS.Item])
        return choice[0]

    def determineWinner(self, user_choice, ai_choice):
        if user_choice == ai_choice:
            print("It's a tie!")
        elif user_choice.losesTo(ai_choice):
            print("You win!")
        else:
            print("AI wins!")