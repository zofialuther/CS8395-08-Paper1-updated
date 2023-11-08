```python
class Hidato:
    board = []
    given = []
    start = []

    @staticmethod
    def main(args):
        input = ["_ 33 35 _ _ . . .",
                 "_ _ 24 22 _ . . .",
                 "_ _ _ 21 _ _ . .",
                 "_ 26 _ 13 40 11 . .",
                 "27 _ _ _ 9 _ 1 .",
                 ". . _ _ 18 _ _ .",
                 ". . . . _ 7 _ _",
                 ". . . . . . 5 _"]

        Hidato.setup(input)
        Hidato.printBoard()
        print("\nFound:")
        Hidato.solve(Hidato.start[0], Hidato.start[1], 1, 0)
        Hidato.printBoard()

    @staticmethod
    def setup(input):
        puzzle = [row.split(" ") for row in input]
        nCols = len(puzzle[0])
        nRows = len(puzzle)

        list = []
        Hidato.board = [[-1 for _ in range(nCols + 2)] for _ in range(nRows + 2)]

        for r in range(nRows):
            row = puzzle[r]
            for c in range(nCols):
                cell = row[c]
                if cell == "_":
                    Hidato.board[r + 1][c + 1] = 0
                elif cell == ".":
                    pass
                else:
                    val = int(cell)
                    Hidato.board[r + 1][c + 1] = val
                    list.append(val)
                    if val == 1:
                        Hidato.start = [r + 1, c + 1]

        list.sort()
        Hidato.given = list

    @staticmethod
    def solve(r, c, n, next):
        if n > Hidato.given[-1]:
            return True

        if Hidato.board[r][c] != 0 and Hidato.board[r][c] != n:
            return False

        if Hidato.board[r][c] == 0 and Hidato.given[next] == n:
            return False

        back = Hidato.board[r][c]
        if back == n:
            next += 1

        Hidato.board[r][c] = n
        for i in range(-1, 2):
            for j in range(-1, 2):
                if Hidato.solve(r + i, c + j, n + 1, next):
                    return True

        Hidato.board[r][c] = back
        return False

    @staticmethod
    def printBoard():
        for row in Hidato.board:
            for c in row:
                if c == -1:
                    print(" . ", end="")
                else:
                    print("%2d " % c if c > 0 else "__ ", end="")
            print()
```