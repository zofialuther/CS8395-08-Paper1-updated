```python
# Langton's ant implementation

# Define possible directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Define possible colors
colors = [0, 1]

# Function to invert the color of a cell
def invert_color(grid, position):
    grid[position[0]][position[1]] = 1 - grid[position[0]][position[1]]

# Function to compute the next direction and position of the ant
def next_move(direction, color):
    if color == 0:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction, (position[0] + directions[direction][0], position[1] + directions[direction][1])

# Function to display the grid
def display_grid(grid):
    for row in grid:
        print(''.join(str(cell) for cell in row))

# Main function
def main(steps):
    grid_size = 20
    grid = [[0] * grid_size for _ in range(grid_size)]
    position = (grid_size // 2, grid_size // 2)
    direction = 0

    for _ in range(steps):
        invert_color(grid, position)
        direction, position = next_move(direction, grid[position[0]][position[1]])
        display_grid(grid)

# Run the simulation for 100 steps
main(100)
```