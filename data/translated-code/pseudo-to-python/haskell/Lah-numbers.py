def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

def lah(n, k):
    if k == 1:
        return factorial(n)
    elif k == n:
        return 1
    elif k > n or k < 1 or n < 1:
        return 0
    else:
        f = factorial(n) * factorial(n-1)
        return f // (factorial(k) * factorial(n-k))

def printLah(n, k):
    if k == 0:
        print(n)
    print(lah(n, k))

def main():
    print("Unsigned Lah numbers: L(n, k):\nn/k")
    zeroToTwelve = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in zeroToTwelve:
        print("        " + str(i))
    for i in zeroToTwelve:
        for j in zeroToTwelve:
            printLah(i, j)
    maxVal = 0
    for i in range(101):
        maxVal = max(maxVal, lah(100, i))
    print("Maximum value from the L(100, *) row:\n" + str(maxVal))