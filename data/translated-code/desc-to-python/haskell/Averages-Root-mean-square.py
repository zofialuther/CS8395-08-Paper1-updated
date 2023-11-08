from math import sqrt
from functools import reduce

def rootMeanSquare(values):
    length = len(values)
    sum_of_squares = reduce(lambda x, y: x + y**2, values, 0)
    return sqrt(sum_of_squares / length)

print(rootMeanSquare(range(1, 11)))