from constraint import Problem

p = Problem()
pvars = "R2 R3 R5 R6 R7 R8 R9 R10 X Y Z".split()
# 0-151 is the possible finite range of the variables
p.addVariables(pvars, range(152))
p.addConstraint(lambda r7, x: r7 == x + 11, ("R7", "X"))
p.addConstraint(lambda r8, y: r8 == y + 11, ("R8", "Y"))
p.addConstraint(lambda r9, y: r9 == y + 4, ("R9", "Y"))
p.addConstraint(lambda r10, z: r10 == z + 4, ("R10", "Z"))
p.addConstraint(lambda r7, r8: r7 + r8 == 40, ("R7", "R8"))
p.addConstraint(lambda r5, r8, r9: r5 == r8 + r9, ("R5", "R8", "R9"))
p.addConstraint(lambda r6, r9, r10: r6 == r9 + r10, ("R6", "R9", "R10"))
p.addConstraint(lambda r2, r5: r2 == 40 + r5, ("R2", "R5"))
p.addConstraint(lambda r3, r5, r6: r3 == r5 + r6, ("R3", "R5", "R6"))
p.addConstraint(lambda r2, r3: r2 + r3 == 151, ("R2", "R3"))
p.addConstraint(lambda y, x, z: y == x + z, ("Y", "X", "Z"))
for sol in p.getSolutionIter():
    print([sol[k] for k in "XYZ"])