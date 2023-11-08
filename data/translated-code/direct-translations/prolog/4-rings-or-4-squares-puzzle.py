import itertools
from constraint import *

# main predicate
def my_sum(Min, Max, Top):
    L = [A, B, C, D, E, F, G]
    problem = Problem()
    problem.addVariables(L, range(Min, Max+1))
    if Top == 0:
        problem.addConstraint(AllDifferentConstraint())
    solutions = problem.getSolutions()
    return solutions

def my_sum_1(Min, Max):
    solutions = my_sum(Min, Max, 0)
    for solution in solutions:
        print(solution)

def my_sum_2(Min, Max, Len):
    solutions = my_sum(Min, Max, 1)
    valid_solutions = [solution for solution in solutions if len(solution) == Len]
    for solution in valid_solutions:
        print(solution)