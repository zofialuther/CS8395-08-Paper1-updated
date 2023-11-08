```python
# map the sequence of cells
def next_cell(x1, y1, x2, y2):
    return (x2, y2)

# map the game items, and how to print
def item(x, y, label):
    return (x, y, label)

# Move - find the current blank space, and the new place and swap them
def move_up(x, y):
    return (x, y+1)

def move_down(x, y):
    return (x, y-1)

def move_left(x, y):
    return (x-1, y)

def move_right(x, y):
    return (x+1, y)

def move(dir, board):
    if dir == "up":
        x, y = [(x, y) for (x, y, p) in board if p == 0][0]
        x1, y1 = move_up(x, y)
    elif dir == "down":
        x, y = [(x, y) for (x, y, p) in board if p == 0][0]
        x1, y1 = move_down(x, y)
    elif dir == "left":
        x, y = [(x, y) for (x, y, p) in board if p == 0][0]
        x1, y1 = move_left(x, y)
    elif dir == "right":
        x, y = [(x, y) for (x, y, p) in board if p == 0][0]
        x1, y1 = move_right(x, y)
    else:
        return None

    p1 = (x, y, 0)
    p2 = (x1, y1, [p for (x, y, p) in board if (x, y) == (x1, y1)][0])

    b1 = [p for p in board if p != (x, y, 0)]
    b1.append(p1)
    b2 = [p for p in b1 if p != (x1, y1, p2[2])]
    b2.append(p2)

    return b2

# Solved - the game is solved if running through the next_cell sequence produces the item sequence.
def solved(board):
    if (1, 1, 1) not in board:
        return False
    remaining = [p for p in board if p != (1, 1, 1)]
    if remaining == [(4, 4, 0)]:
        return True
    else:
        x, y, prev = [(x, y, p) for (x, y, p) in board if p == 0][0]
        _, p, _ = [(x, y, p) for (x, y, p) in board if (x, y) == (x, y)][0]
        if (x, y, p) not in remaining:
            return False
        x1, y1 = next_cell(x, y, x, y)
        return solved(remaining)

# Print - run through the next_cell sequence printing the found items.
def print_board(board):
    p1 = [(x, y, p) for (x, y, p) in board if (x, y) == (1, 1)][0]
    print(p1[2])
    remaining = [p for p in board if p != (1, 1, p1[2])]
    x, y, _ = [(x, y, p) for (x, y, p) in board if p == 0][0]
    while remaining:
        x1, y1 = next_cell(x, y, x, y)
        p2 = [(x1, y1, p) for (x1, y1, p) in board if (x1, y1) == (x1, y1)][0]
        print(p2[2])
        x, y = x1, y1
        remaining = [p for p in board if p != (x, y, p2[2])]

# Next Move - get the player input.
def next_move_by_player():
    while True:
        char = input("Enter a move (w, a, s, d): ")
        if char in ['w', 'a', 's', 'd']:
            return char

# Play - loop over the player moves until solved.
def play(board):
    if solved(board):
        print_board(board)
        print('You Win!')
    else:
        print_board(board)
        move = next_move_by_player()
        new_board = move(move, board)
        play(new_board)

def test_board():
    return [(1, 1, 9), (2, 1, 1), (3, 1, 4), (4, 1, 7),
            (1, 2, 6), (2, 2, 5), (3, 2, 3), (4, 2, 2),
            (1, 3, 13), (2, 3, 10), (3, 3, 0), (4, 3, 8),
            (1, 4, 14), (2, 4, 15), (3, 4, 11), (4, 4, 12)]

play(test_board())
```