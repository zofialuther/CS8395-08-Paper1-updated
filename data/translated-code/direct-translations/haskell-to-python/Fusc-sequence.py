def fusc(i):
    if i < 1:
        return 0
    else:
        return go(i-1)[0]

def go(n):
    if n == 0:
        return (1, 0)
    elif n % 2 == 0:
        x, y = go(n // 2)
        return (x + y, y)
    else:
        x, y = go(n // 2)
        return (x, x + y)

def main():
    print("First 61 terms:")
    print([fusc(x) for x in range(61)])
    print("\n(Index, Value):")
    for i, x in take(5, widths):
        print((i, x))

def widths():
    return map(lambda x: (x[1], x[2]), iterate(nxtWidth, (2, 0, 0)))

def nxtWidth(w, i, v):
    w = w + 1
    fi = lambda i: (i, fusc(i))
    j, x = until(lambda x: w <= len(str(x[1])), lambda x: fi(x[0] + 1), (i, fusc(i)))

main()