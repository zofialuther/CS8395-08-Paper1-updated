```python
from itertools import permutations

def nono(RowSpec, ColSpec, Grid):
    rows(RowSpec, Grid)
    GridT = list(zip(*Grid))
    rows(ColSpec, GridT)

def rows(spec, grid):
    if not spec:
        return
    else:
        row(spec[0], grid[0])
        rows(spec[1:], grid[1:])

def row(ks, row):
    ones = sum(ks)
    RowZ = row + [0]
    automaton(RowZ, ks, ones)

def automaton(row, ks, ones):
    arcs = []
    cur_state = 'start'
    final_state = 'Final'
    for k in ks:
        next_state = 'state' + str(ks.index(k))
        if k == 0:
            arcs.extend([(cur_state, 0, cur_state), (cur_state, 0, next_state)])
        else:
            arcs.append((cur_state, 1, next_state))
            k1 = k-1
            automaton([k1]+ks[ks.index(k)+1:], row, next_state, final_state)
    return arcs

def make_grid(x, y):
    grid = [[0]*y for _ in range(x)]
    return grid

def print_grid(grid):
    for row in grid:
        print_row(row)

def print_row(row):
    for x in row:
        if x == 0:
            print(' ', end='')
        else:
            print('x', end='')
    print('')

def nonogram(rows, cols):
    x = len(rows)
    y = len(cols)
    grid = make_grid(x, y)
    nono(rows, cols, grid)
    print_grid(grid)

# Example usage
rows = [[3], [2,2], [1,1], [3], [1]]
cols = [[1], [3], [2], [2], [1]]
nonogram(rows, cols)
```