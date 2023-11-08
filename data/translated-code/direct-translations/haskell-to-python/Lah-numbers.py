from functools import reduce
from operator import mul

def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(mul, range(1, n+1))

def lah(n, k):
    if k == 1:
        return factorial(n)
    elif k == n:
        return 1
    elif k > n or k < 1 or n < 1:
        return 0
    else:
        f = reduce(mul, range(1, n+1)) // (reduce(mul, range(1, k+1)) * factorial(n - k))
        return f

def print_lah(n, k):
    if k == 0:
        print("\n%3d" % n, end="")
    print("%11d" % lah(n, k), end="")

def main():
    print("Unsigned Lah numbers: L(n, k):\nn/k")
    for i in range(13):
        print("%11d" % i, end="")
    for i in range(13):
        for j in range(13):
            print_lah(i, j)
    print("\nMaximum value from the L(100, *) row:")
    print(max(lah(100, j) for j in range(101)))

if __name__ == "__main__":
    main()