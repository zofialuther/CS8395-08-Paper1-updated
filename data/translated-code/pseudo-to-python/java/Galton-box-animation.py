class GaltonBox:
    def __init__(self, pinRows, ballCount):
        self.m_pinRows = pinRows
        self.m_startRow = pinRows + 1
        self.m_balls = [Position(self.m_startRow, 0, 'o') for _ in range(ballCount)]

    def run(self):
        ballsInPlay = len(self.m_balls)
        while ballsInPlay > 0:
            ballsInPlay = self.dropBalls()
            self.print()

    def dropBalls(self):
        ballsInPlay = 0
        ballToStart = -1

        for i, ball in enumerate(self.m_balls):
            if ball.m_row == self.m_startRow:
                ballToStart = i

        for i, ball in enumerate(self.m_balls):
            if i == ballToStart:
                ball.m_row = self.m_pinRows
                ballsInPlay += 1
            elif ball.m_row > 0 and ball.m_row != self.m_startRow:
                ball.m_row -= 1
                ball.m_col += random.randint(0, 1)
                if ball.m_row != 0:
                    ballsInPlay += 1

        return ballsInPlay

    def print(self):
        for row in range(self.m_startRow, 0, -1):
            for ball in self.m_balls:
                if ball.m_row == row:
                    self.printBall(ball)
            self.printPins(row)

        self.printCollectors()

    def printBall(self, pos):
        print(' ' * (pos.m_row + 1), end='')
        for col in range(pos.m_col + 1):
            print('  ', end='')
        print(pos.m_char)

    def printPins(self, row):
        print(' ' * (row + 1), end='')
        for col in range(self.m_startRow - row, -1, -1):
            print('. ', end='')

    def printCollectors(self):
        collectors = [[] for _ in range(self.m_startRow + 1)]

        for col in range(self.m_startRow + 1):
            collector = []
            for ball in self.m_balls:
                if ball.m_row == 0 and ball.m_col == col:
                    collector.append(ball)
            collectors[col] = collector

        rows = self.longest(collectors)
        for row in range(rows):
            for col in range(self.m_startRow + 1):
                collector = collectors[col]
                pos = row + len(collector) - rows
                print('|', end='')
                if pos >= 0:
                    print(collector[pos].m_char, end='')
                else:
                    print(' ', end='')
            print('|')

    def longest(self, collectors):
        result = 0
        for collector in collectors:
            result = max(len(collector), result)
        return result