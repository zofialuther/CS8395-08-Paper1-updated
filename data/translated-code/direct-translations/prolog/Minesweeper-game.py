```python
from itertools import permutations
import random

def play(W, H):
    print('''
Welcome to prolog minesweeper!
: o X Y  exposes a cell of the grid
: m X Y  marks bombs

Any else to quit.
''')

    grid = make_grid(W, H)
    play_game(grid)

def play_game(grid):
    if map_grid(won, grid):
        map_grid(print_cell, grid)
        print('you won!')
    elif not map_grid(still_playing, grid):
        map_grid(print_cell, grid)
        print('you hit a bomb!')
    else:
        map_grid(print_cell, grid)
        op, X, Y = parse_input()
        grid2 = do_op(op, (X, Y), grid)
        play_game(grid2)

def make_grid(W, H):
    cells = ['.'] * (W * H)
    NBombs = W * H // 5
    print(f'There are {NBombs} bombs on the grid')
    all_bombs = ['?'] * NBombs
    new_cells = map_bombs_to_cells(cells, all_bombs)
    random.shuffle(new_cells)
    created_cells = convert_col(new_cells, W, H)
    mapped_cells = map_grid(adj_bomb, grid(W, H, created_cells))
    return grid(W, H, mapped_cells)

def map_bombs_to_cells(cells, bombs):
    new_cells = []
    for cell, bomb in zip(cells, bombs):
        new_cells.append(bomb)
    return new_cells

def convert_row(T, W):
    if W == 0:
        return [], T
    else:
        return [T[0]] + convert_row(T[1:], W-1)

def convert_col(C, W, H):
    if H == 0:
        return []
    else:
        row, rest = convert_row(C, W)
        return [row] + convert_col(rest, W, H-1)

def adj_bomb(p, D, Cell):
    if Cell == '?':
        return '.'
    x, y = p
    bombs = []
    for Ax in range(1, D[0]+1):
        for Ay in range(1, D[1]+1):
            if (Ax, Ay) != (x, y) and grid_val_xy(grid, (Ax, Ay)) == '?':
                bombs.append((Ax, Ay))
    return len(bombs)

# other functions and classes need to be implemented as well
```