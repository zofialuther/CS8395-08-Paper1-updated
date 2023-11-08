from functools import lru_cache

@lru_cache(maxsize=None)
def stirling1(n, k):
    if n == 0 and k == 0:
        return 1
    elif n > 0 and k == 0:
        return 0
    elif k > n:
        return 0
    else:
        return stirling1(n-1, k-1) + (n-1) * stirling1(n-1, k)

def main():
    print("n/k", end='')
    for i in range(13):
        print(f"{i:10d}", end='')
    print()
    print("-" * (13 * 10 + 3))
    table = [(i, j) for i in range(13) for j in range(13)]
    for row in table:
        print(f"{row[0]:2d}|", end='')
        for col in table:
            print(f"{stirling1(col[0], col[1]):10d}", end='')
        print()
    max_val = max(stirling1(100, n) for n in range(1, 101))
    print(f"\nThe maximum value of S1(100, k):\n{max_val}")

if __name__ == "__main__":
    main()