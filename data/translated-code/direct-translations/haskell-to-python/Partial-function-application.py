from functools import map

def f1(x):
    return x * 2

def f2(x):
    return x ** 2

fsf1 = map(f1)
fsf2 = map(f2)

print(list(fsf1([0, 1, 2, 3]))  # prints [0, 2, 4, 6]
print(list(fsf2([0, 1, 2, 3]))  # prints [0, 1, 4, 9]
print(list(fsf1([2, 4, 6, 8]))  # prints [4, 8, 12, 16]
print(list(fsf2([2, 4, 6, 8]))  # prints [4, 16, 36, 64]