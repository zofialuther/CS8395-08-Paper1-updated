```python
from constraint import *

problem = Problem()

def caesar_cipher(x, y):
    problem.addVariable(x, y)

problem.addConstraint(caesar_cipher, ("A", "D"))
problem.addConstraint(caesar_cipher, ("B", "E"))
problem.addConstraint(caesar_cipher, ("C", "F"))
# ... continue adding constraints for the rest of the alphabet

problem.getSolutions()
```