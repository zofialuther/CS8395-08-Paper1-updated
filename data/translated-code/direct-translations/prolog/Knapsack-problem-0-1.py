import itertools

from constraint import *

problem = Problem()

items = [
    ("map", 9, 150),
    ("compass", 13, 35),
    ("water", 153, 200),
    ("sandwich", 50, 160),
    ("glucose", 15, 60),
    ("tin", 68, 45),
    ("banana", 27, 60),
    ("apple", 39, 40),
    ("cheese", 23, 30),
    ("beer", 52, 10),
    ("suntan cream", 11, 70),
    ("camera", 32, 30),
    ("t-shirt", 24, 15),
    ("trousers", 48, 10),
    ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70),
    ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80),
    ("sunglasses", 7, 20),
    ("towel", 18, 12),
    ("socks", 4, 50),
    ("book", 30, 10)
]

problem.addVariables(range(len(items)), [0, 1])

problem.addConstraint(
    lambda *values: sum(items[i][1] for i, value in enumerate(values) if value == 1) <= 400,
    range(len(items))
)

problem.addConstraint(
    lambda *values: sum(items[i][2] for i, value in enumerate(values) if value == 1) >= 400,
    range(len(items))
)

solutions = problem.getSolutions()

for solution in solutions:
    print([items[i] for i, value in solution.items() if value == 1])