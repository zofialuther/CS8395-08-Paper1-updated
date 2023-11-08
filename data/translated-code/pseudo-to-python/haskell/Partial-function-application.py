def fs(array, func):
    return list(map(func, array))

def f1(x):
    return x * 2

def f2(x):
    return x ** 2

def main():
    fsf1 = fs([0, 1, 2, 3], f1)
    fsf2 = fs([0, 1, 2, 3], f2)
    print(fsf1) # prints [0, 2, 4, 6]
    print(fsf2) # prints [0, 1, 4, 9]
    fsf1 = fs([2, 4, 6, 8], f1)
    fsf2 = fs([2, 4, 6, 8], f2)
    print(fsf1) # prints [4, 8, 12, 16]
    print(fsf2) # prints [4, 16, 36, 64]

main()