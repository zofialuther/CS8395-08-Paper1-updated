import constraint

problem = constraint.Problem()

# Initialize the 10x10 grid
grid = [[0 for _ in range(10)] for _ in range(10)]

# Apply constraints to ensure valid Hidato puzzle
# Add constraints using CLPFD

# Solve the puzzle
solution = problem.getSolution()

# Function to display the result
def display_result(grid):
    for row in grid:
        print(row)