```python
import random

class GaltonBox:
    def __init__(self, pinRows, ballCount):
        self.m_pinRows = pinRows
        self.m_startRow = pinRows + 1
        self.m_balls = [Position(self.m_startRow, 0, 'o') for _ in range(ballCount)]
        self.m_random = random.Random()

    def run(self):
        ballsInPlay = len(self.m_balls)
        while ballsInPlay > 0:
            ballsInPlay = self.dropBalls()
            self.print()

    def dropBalls(self):
        ballsInPlay = 0
        ballToStart = -1

        for ball in range(len(self.m_balls)):
            if self.m_balls[ball].m_row == self.m_startRow:
                ballToStart = ball

        for ball in range(len(self.m_balls)):
            if ball == ballToStart:
                self.m_balls[ball].m_row = self.m_pinRows
                ballsInPlay += 1
            elif self.m_balls[ball].m_row > 0 and self.m_balls[ball].m_row != self.m_startRow:
                self.m_balls[ball].m_row -= 1
                self.m_balls[ball].m_col += self.m_random.randint(0, 1)
                if self.m_balls[ball].m_row != 0:
                    ballsInPlay += 1

        return ballsInPlay

    def print(self):
        for row in range(self.m_startRow, 0, -1):
            for ball in self.m_balls:
                if ball.m_row == row:
                    self.printBall(ball)
            print()
            self.printPins(row)
        self.printCollectors()
        print()

    @staticmethod
    def printBall(pos):
        for col in range(pos.m_row + 1, -1, -1):
            print(' ', end='')
        for col in range(pos.m_col):
            print('  ', end='')
        print(pos.m_char)

    def printPins(self, row):
        for col in range(row + 1, -1, -1):
            print(' ', end='')
        for col in range(self.m_startRow - row, -1, -1):
            print('. ', end='')
        print()

    def printCollectors(self):
        collectors = [[] for _ in range(self.m_startRow)]

        for col in range(self.m_startRow):
            collector = []
            for ball in self.m_balls:
                if ball.m_row == 0 and ball.m_col == col:
                    collector.append(ball)
            collectors[col] = collector

        rows = max(len(collector) for collector in collectors)
        for row in range(rows):
            for col in range(self.m_startRow):
                collector = collectors[col]
                pos = row + len(collector) - rows
                print('|', end='')
                if pos >= 0:
                    print(collector[pos].m_char, end='')
                else:
                    print(' ', end='')
            print('|')

    @staticmethod
    def longest(collectors):
        return max(len(collector) for collector in collectors)

class Position:
    def __init__(self, row, col, ch):
        self.m_row = row
        self.m_col = col
        self.m_char = ch

if __name__ == "__main__":
    GaltonBox(8, 200).run()
```