```python
# map the sequence of cells
def next_cell(x1, y, x2, y):
    return (x1, y, x2, y)

# map the game items, and how to print
def item(x1, y, value):
    return (x1, y, value)

# Move - find the current blank space, and the new place and swap them
def move_1(x1, x2):
    return (x1, x2)

def move(direction, board):
    pass

# Solved - the game is solved if running through the next_cell sequence produces the item sequence.
def solved(board):
    pass

# Print - run through the next_cell sequence printing the found items.
def print(board):
    pass

# Next Move - get the player input.
def next_move_by_player(move):
    pass

# Play - loop over the player moves until solved.
def play(board):
    pass

def play():
    pass

def test_board(board):
    pass
```