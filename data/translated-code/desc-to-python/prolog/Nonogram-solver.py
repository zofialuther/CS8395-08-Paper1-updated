```python
# Python code for nonogram/paint-by-numbers solver using the CLP(FD) constraint library

from constraint import *

# Function to create a grid
def create_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid

# Function to solve the nonogram puzzle
def solve_nonogram(grid, row_specs, col_specs):
    problem = Problem()
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        problem.addConstraint(ExactSumConstraint(row_specs[i]), [grid[i][j] for j in range(cols)])
    
    for j in range(cols):
        problem.addConstraint(ExactSumConstraint(col_specs[j]), [grid[i][j] for i in range(rows)])
    
    solution = problem.getSolution()
    return solution

# Function to print the solved grid
def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))
```