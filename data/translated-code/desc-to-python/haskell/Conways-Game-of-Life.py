```python
def grid(initial_state):
    return [[c for c in row] for row in initial_state]

def printGrid(grid):
    for row in grid:
        print(''.join(row))

def printLife(grid, generations):
    for _ in range(generations):
        printGrid(grid)
        # logic for simulating game
        # ...
        # update grid for next generation
        # ...

def main():
    glider = [
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        ".........."
    ]
    initial_grid = grid(glider)
    printLife(initial_grid, 10)

main()
```