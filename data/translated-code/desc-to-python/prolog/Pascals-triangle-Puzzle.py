```python
from constraint import *

problem = Problem()

problem.addVariable('X', [1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable('Y', [1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable('Z', [1, 2, 3, 4, 5, 6, 7, 8, 9])

problem.addConstraint(lambda x, y, z: y == x + z, ('X', 'Y', 'Z'))

solutions = problem.getSolutions()
print(solutions)
```