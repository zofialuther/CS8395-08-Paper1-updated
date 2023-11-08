import random
import math

class FuzzyCircle:
    rnd = random.Random()

    def main(self):
        field = [[' ' for _ in range(31)] for _ in range(31)]
        pointsInDisc = 0
        while pointsInDisc < 100:
            x = self.rnd.randint(0, 30) - 15
            y = self.rnd.randint(0, 30) - 15
            dist = math.hypot(x, y)
            if 10 <= dist <= 15 and field[x + 15][y + 15] == ' ':
                field[x + 15][y + 15] = 'X'
                pointsInDisc += 1
        for row in field:
            print(''.join(row))

fuzzy_circle = FuzzyCircle()
fuzzy_circle.main()