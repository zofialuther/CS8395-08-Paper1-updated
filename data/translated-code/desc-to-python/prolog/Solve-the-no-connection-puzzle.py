```python
from constraint import Problem, AllDifferentConstraint

# Define nodes and edges

problem = Problem()
nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]

# Add variables to the problem
problem.addVariables(nodes, range(1, 5))

# Add constraint that connected nodes have different values by more than 1
for edge in edges:
    problem.addConstraint(lambda x, y: abs(x - y) > 1, (edge[0], edge[1]))

# Solve the puzzle
solutions = problem.getSolutions()
print(solutions)
```