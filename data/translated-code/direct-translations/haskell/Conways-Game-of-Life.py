from typing import List, Tuple
from itertools import islice

def grid(l: List[str]) -> Tuple[int, int, list]:
    width, height = len(l[0]), len(l)
    a = [[False if x == '.' else True for x in row] for row in l]
    return (width, height, a)

def printGrid(width: int, grid: list) -> None:
    for row in grid:
        print(''.join(['.' if cell == False else '#' for cell in row]))

def split(n: int, a: list) -> List[List]:
    return [a[i:i+n] for i in range(0, len(a), n)]

blinker = grid([
    ".#.",
    ".#.",
    ".#."
])

glider = grid([
    "............",
    "............",
    "............",
    ".......###..",
    ".......#....",
    "........#...",
    "............"
])

def life(width: int, height: int, grid: list) -> list:
    new_grid = [[False for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            live_neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < height and 0 <= j + y < width and grid[i + x][j + y]:
                        live_neighbors += 1
            if grid[i][j]:
                new_grid[i][j] = live_neighbors in [2, 3]
            else:
                new_grid[i][j] = live_neighbors == 3
    return new_grid

def printLife(n: int, w: int, h: int, g: list) -> None:
    current_grid = g
    for _ in range(n):
        printGrid(w, current_grid)
        current_grid = life(w, h, current_grid)

printLife(10, len(glider[0]), len(glider[1]), glider)