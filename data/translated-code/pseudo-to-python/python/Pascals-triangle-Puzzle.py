```python
from constraint import Problem

p = Problem()
pvars = "R2 R3 R5 R6 R7 R8 R9 R10 X Y Z".split()
p.addVariables(pvars, range(152))
p.addConstraint(lambda R7, X: R7 == X + 11, ("R7", "X"))
p.addConstraint(lambda R8, Y: R8 == Y + 11, ("R8", "Y"))
p.addConstraint(lambda R9, Y: R9 == Y + 4, ("R9", "Y"))
p.addConstraint(lambda R10, Z: R10 == Z + 4, ("R10", "Z"))
p.addConstraint(lambda R7, R8: R7 + R8 == 40, ("R7", "R8"))
p.addConstraint(lambda R5, R8, R9: R5 == R8 + R9, ("R5", "R8", "R9"))
p.addConstraint(lambda R6, R9, R10: R6 == R9 + R10, ("R6", "R9", "R10"))
p.addConstraint(lambda R2, R5: R2 == 40 + R5, ("R2", "R5"))
p.addConstraint(lambda R3, R5, R6: R3 == R5 + R6, ("R3", "R5", "R6"))
p.addConstraint(lambda R2, R3: R2 + R3 == 151, ("R2", "R3"))
p.addConstraint(lambda Y, X, Z: Y == X + Z, ("Y", "X", "Z"))
for sol in p.getSolutionIter():
    print([sol[k] for k in "XYZ"])
```