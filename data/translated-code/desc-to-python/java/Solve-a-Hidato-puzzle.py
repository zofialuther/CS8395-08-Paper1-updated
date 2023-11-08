class Hidato:
    def __init__(self, input):
        self.board = []
        self.givenValues = []
        self.setup(input)
        self.printBoard()
        self.solve()

    def setup(self, input):
        # parse input to create initial board state and list of given values
        pass

    def solve(self):
        # use backtracking to recursively solve the puzzle
        pass

    def printBoard(self):
        # print current state of the board to the console
        pass