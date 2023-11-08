```python
class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [[0 for _ in range(N)] for _ in range(N)]

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def print_board(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.board[i][j], end=" ")
            print()

    def solve_nqueens(self):
        if not self.solve_nqueens_util(0):
            print("No solution exists")

    def solve_nqueens_util(self, col):
        if col == self.N:
            self.print_board()
            print()
            return True
        res = False
        for i in range(self.N):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve_nqueens_util(col + 1) or res
                self.board[i][col] = 0
        return res

if __name__ == "__main__":
    nqueens = NQueens(8)
    nqueens.solve_nqueens()
```