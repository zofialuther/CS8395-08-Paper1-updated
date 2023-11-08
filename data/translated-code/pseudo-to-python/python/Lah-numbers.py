def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def lah(n, k):
    if k == 1:
        return factorial(n)
    elif k == n:
        return 1
    elif k > n:
        return 0
    elif k < 1 or n < 1:
        return 0
    else:
        return comb(n, k) * factorial(n - 1) // factorial(k - 1)

def main():
    print("Unsigned Lah numbers: L(n, k):")
    print("n/k ", end='\t')
    for i in range(13):
        print("%11d" % i, end='\t')
    print()
    for row in range(13):
        print("%-4d" % row, end='\t')
        for i in range(row+1):
            l = lah(row, i)
            print("%11d" % l, end='\t')
        print()
    print("\nMaximum value from the L(100, *) row:")
    max_val = max(lah(100, a) for a in range(100))
    print(max_val)

if __name__ == '__main__':
    main()