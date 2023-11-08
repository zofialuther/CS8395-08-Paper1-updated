from math import sqrt
from functools import reduce

def rootMeanSquare(numbers):
    return sqrt(reduce(lambda x, y: x + y**2, numbers, 0) / len(numbers)

if __name__ == "__main__":
    print(rootMeanSquare(list(range(1, 11))))