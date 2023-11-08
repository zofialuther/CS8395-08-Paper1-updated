```python
def replace(lst, n, e):
    if n == 0:
        lst[0] = e
    else:
        lst[1] = replace(lst[1], n-1, e)
    return lst

def replace_in(grid, coords, e):
    x, y = coords
    grid[x] = replace(grid[x], y, e)
    return grid

def get_in(grid, coords):
    x, y = coords
    return grid[x][y]

def create(n):
    return [[None for _ in range(n)] for _ in range(n)]

def ops(direction, coords):
    x, y = coords
    if direction == 'right':
        return (x, y+1), (x+1, y), 'right', 'down'
    elif direction == 'left':
        return (x, y-1), (x-1, y), 'left', 'up'
    elif direction == 'up':
        return (x-1, y), (x, y+1), 'up', 'right'
    elif direction == 'down':
        return (x+1, y), (x, y-1), 'down', 'left'

def next(direction, grid, coords):
    c1, c2, d1, d2 = ops(direction, coords)
    if get_in(grid, c1) == None:
        return c1, d1
    else:
        return c2, d2

def spiralH(direction, grid, coords, values):
    grid = replace_in(grid, coords, values[0])
    if len(values) == 1:
        return grid
    else:
        new_coords, new_direction = next(direction, grid, coords)
        return spiralH(new_direction, grid, new_coords, values[1:])

def spiral(n):
    values = list(range(n*n))
    grid = create(n)
    return spiralH('right', grid, (0, 0), values)
```