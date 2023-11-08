import random

class Monty:
    @staticmethod
    def main(args):
        switchWins = 0
        stayWins = 0
        gen = random.Random()
        for plays in range(32768):
            doors = [0, 0, 0]
            doors[gen.randint(0, 2)] = 1
            choice = gen.randint(0, 2)
            shown = 0
            while True:
                shown = gen.randint(0, 2)
                if shown != choice and doors[shown] != 1:
                    break
            stayWins += doors[choice]
            switchWins += doors[3 - choice - shown]
        print("Switching wins", switchWins)
        print("Staying wins", stayWins)