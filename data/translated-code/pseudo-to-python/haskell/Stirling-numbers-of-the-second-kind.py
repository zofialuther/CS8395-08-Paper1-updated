from Data.List import groupBy
import Data.MemoCombinators as Memo
import Text.Printf

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
        return k * stirling2(n-1, k) + stirling2(n-1, k-1)

def main():
    print("n/k")
    for i in range(13):
        printf("%10d" % i)
    printf("\n")
    print("%s" % ('-' * (13 * 10 + 3)))
    table = groupBy(lambda a, b: a[0] == b[0], [(i, j) for i in range(13) for j in range(13)])
    for row in table:
        printf("%2d|" % row[0][0])
        for r in row:
            printf("%10d" % stirling2(r[0], r[1]))
        printf("\n")
    max_val = max([stirling2(100, n) for n in range(1, 101)])
    printf("\nThe maximum value of S2(100, k):\n%d\n" % max_val)

if __name__ == "__main__":
    main()