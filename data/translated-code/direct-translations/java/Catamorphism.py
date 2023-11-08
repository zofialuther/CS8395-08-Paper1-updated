from functools import reduce

def multiply(a, b):
    return a * b

numbers = [1, 2, 3, 4, 5]

print(sum(numbers))
print(reduce(multiply, numbers))