from functools import reduce

myIntArray = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, map(lambda x: x**3, myIntArray))
print("sum:", sum)