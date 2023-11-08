def perfect(n):
    root = int(n ** 0.5)
    lows = []
    for x in range(2, root + 1):
        if n % x == 0:
            lows.append(x)
    sumLows = sum(lows)
    highs = []
    for x in lows:
        if root != x:
            highs.append(n // x)
    sumHighs = sum(highs)
    return n > 1 and n == 1 + sumLows + sumHighs

def main():
    result = []
    for x in range(1, 10001):
        if perfect(x):
            result.append(x)
    print(result)

def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))

if __name__ == '__main__':
    main()