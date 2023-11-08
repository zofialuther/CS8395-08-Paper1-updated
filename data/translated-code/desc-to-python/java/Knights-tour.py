```python
import random

def is_valid_move(board, n, x, y):
    return x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1

def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

def solve_knights_tour(n):
    board = [[-1 for i in range(n)] for j in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1
    if not solve_knights_tour_util(board, n, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        print_solution(board)

def solve_knights_tour_util(board, n, curr_x, curr_y, move_x, move_y, pos):
    if pos == n**2:
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_valid_move(board, n, new_x, new_y):
            board[new_x][new_y] = pos
            if solve_knights_tour_util(board, n, new_x, new_y, move_x, move_y, pos+1):
                return True
            board[new_x][new_y] = -1
    return False

n = 8
solve_knights_tour(n)
```