from random import Random

class FuzzyCircle:
    rnd = Random()

    @staticmethod
    def main(args):
        field = [[' ' for i in range(31)] for j in range(31)]
        pointsInDisc = 0

        while pointsInDisc < 100:
            x = FuzzyCircle.rnd.randint(-15, 15)
            y = FuzzyCircle.rnd.randint(-15, 15)
            distance = ((x ** 2) + (y ** 2)) ** 0.5

            if 10 <= distance <= 15 and field[x + 15][y + 15] == ' ':
                field[x + 15][y + 15] = 'X'
                pointsInDisc += 1

        for row in field:
            for element in row:
                print(element, end='')
            print()
            
FuzzyCircle.main([])