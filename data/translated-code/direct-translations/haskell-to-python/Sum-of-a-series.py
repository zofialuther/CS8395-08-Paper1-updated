def seriesSum(f):
    return functools.reduce(lambda x, y: (f(y) + x), range(1, 1001), 0)

def inverseSquare(x):
    return 1 / (x ** 2)

def main():
    print(seriesSum(inverseSquare))

if __name__ == "__main__":
    main()