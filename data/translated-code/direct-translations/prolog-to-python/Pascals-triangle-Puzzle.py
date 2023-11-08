import itertools
from constraint import *

def puzzle():
    problem = Problem()
    problem.addVariable('X', range(1, 10))
    problem.addVariable('Y', range(1, 10))
    problem.addVariable('Z', range(1, 10))
    problem.addConstraint(lambda x, y, z: x + y == z, ('X', 'Y', 'Z'))
    solutions = problem.getSolutions()
    return solutions

print(puzzle())