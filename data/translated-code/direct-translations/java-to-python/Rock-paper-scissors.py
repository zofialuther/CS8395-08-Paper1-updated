from enum import Enum
import random

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    # LIZARD = 4
    # SPOCK = 5

    def __init__(self):
        self.losesToList = []

    def losesTo(self, other):
        return other in self.losesToList

RPS.SCISSORS.losesToList = [RPS.ROCK, RPS.SPOCK]
RPS.ROCK.losesToList = [RPS.PAPER, RPS.SPOCK]
RPS.PAPER.losesToList = [RPS.SCISSORS, RPS.LIZARD]
# RPS.SPOCK.losesToList = [RPS.PAPER, RPS.LIZARD]
# RPS.LIZARD.losesToList = [RPS.SCISSORS, RPS.ROCK]

counts = {RPS.ROCK: 1, RPS.PAPER: 1, RPS.SCISSORS: 1}
totalThrows = len(RPS)

def run():
    print("Make your choice: ")
    while True:
        aiChoice = getAIChoice()
        input_str = input()
        try:
            choice = RPS[input_str.upper()]
        except KeyError:
            print("Invalid choice")
            continue
        counts[choice] += 1
        totalThrows += 1
        print("Computer chose: ", aiChoice)
        if aiChoice == choice:
            print("Tie!")
        elif aiChoice.losesTo(choice):
            print("You chose...wisely. You win!")
        else:
            print("You chose...poorly. You lose!")
        print("Make your choice: ")

def getAIChoice():
    rand = random.randint(0, totalThrows - 1)
    for item, count in counts.items():
        if rand < count:
            losesTo = item.losesToList
            return random.choice(losesTo)
        rand -= count
    return None

run()