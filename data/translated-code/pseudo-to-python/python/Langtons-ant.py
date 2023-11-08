from enum import Enum

class Dir(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Color(Enum):
    BLACK = 0
    WHITE = 1

def invert_color(grid, x, y):
    if grid[y][x] == Color.BLACK:
        grid[y][x] = Color.WHITE
    else:
        grid[y][x] = Color.BLACK

def next_direction(grid, x, y, direction):
    if grid[y][x] == Color.BLACK:
        turn_right = False
    else:
        turn_right = True
    direction_index = direction.value
    if turn_right:
        direction_index = (direction_index + 1) % 4
    else:
        direction_index = (direction_index - 1) % 4
    directions = [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT]
    direction = directions[direction_index]
    return direction

def next_position(x, y, direction):
    if direction == Dir.UP:
        y = y - 1
    elif direction == Dir.RIGHT:
        x = x + 1
    elif direction == Dir.DOWN:
        y = y + 1
    elif direction == Dir.LEFT:
        x = x - 1
    return x, y

def print_grid(grid):
    print(80 * "#")
    print("\n".join("".join(v.name for v in row) for row in grid))

def ant(width, height, max_nb_steps):
    grid = [[Color.WHITE for _ in range(width)] for _ in range(height)]
    x = width // 2
    y = height // 2
    direction = Dir.UP
    i = 0
    while i < max_nb_steps and 0 <= x < width and 0 <= y < height:
        invert_color(grid, x, y)
        direction = next_direction(grid, x, y, direction)
        x, y = next_position(x, y, direction)
        print_grid(grid)
        i = i + 1

if __name__ == "__main__":
    ant(width=75, height=52, max_nb_steps=12000)