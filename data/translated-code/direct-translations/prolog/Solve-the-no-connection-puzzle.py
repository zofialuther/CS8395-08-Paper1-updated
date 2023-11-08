from itertools import permutations
from constraint import *

problem = Problem()
problem.addVariable('a', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('b', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('c', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('d', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('e', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('f', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('g', [1, 2, 3, 4, 5, 6, 7, 8])
problem.addVariable('h', [1, 2, 3, 4, 5, 6, 7, 8])

problem.addConstraint(AllDifferentConstraint(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

def connected(a, b):
    return (a, b) in edges or (b, a) in edges

def set_constraints(lst, values):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if connected(lst[i], lst[j]):
                problem.addConstraint(lambda x, y: abs(x - y) > 1, (values[lst.index(lst[i])], values[lst.index(lst[j])]))

edges = [('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'g'), ('d', 'e'), ('d', 'g'), ('d', 'h'), ('e', 'f'), ('e', 'g'), ('e', 'h'), ('f', 'h')]

lst = list(set([x[0] for x in edges] + [x[1] for x in edges]))
values = list('abcdefgh')

set_constraints(lst, values)

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)