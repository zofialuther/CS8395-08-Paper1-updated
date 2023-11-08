```python
import numpy as np
import matplotlib.pyplot as plt
from constraint import Problem, AllDifferentConstraint

problem = Problem()

problem.addVariable('x', range(400))
problem.addVariable('y', range(400))

def circle_constraint(x, y):
    return 100 <= x**2 + y**2 <= 225

problem.addConstraint(circle_constraint, ['x', 'y'])

solution = problem.getSolution()

plt.scatter(solution['x'], solution['y'])
plt.xlim(0, 400)
plt.ylim(0, 400)
plt.show()
```