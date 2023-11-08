from functools import reduce

def seriesSum(f, lst):
    return reduce(lambda x, y: x + f(y), lst, 0)

def inverseSquare(x):
    return 1 / (x ** 2)

def main():
    result = seriesSum(inverseSquare, [i for i in range(1, 1001)])
    print(result)

main()