from memoization import cached

@cached
def stirling2(n, k):
    if n == 0 and k == 0:
        return 1
    elif (n > 0 and k == 0) or (n == 0 and k > 0):
        return 0
    elif n == k:
        return 1
    elif k > n:
        return 0
    else:
        return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

def main():
    print("n/k", end="")
    for i in range(13):
        print(f"{i:10d}", end="")
    print()
    print("-" * (13 * 10 + 3))
    table = [(i, j) for i in range(13) for j in range(13)]
    for row in table:
        print(f"{row[0]:2d}|", end="")
        for val in row:
            print(f"{stirling2(*val):10d}", end="")
        print()
    max_val = max([stirling2(100, n) for n in range(1, 101)])
    print(f"\nThe maximum value of S2(100, k):\n{max_val}")

if __name__ == "__main__":
    main()