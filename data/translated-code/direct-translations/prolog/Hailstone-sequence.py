def hailstone(n, result):
    result.append(n)
    if n == 1:
        return
    if n % 2 == 0:
        hailstone(n//2, result)
    else:
        hailstone(3*n + 1, result)

X = []
hailstone(27, X)
if len(X) == 112 and X[:4] == [27, 82, 41, 124] and X[-4:] == [8, 4, 2, 1]:
    print("Valid sequence")
else:
    print("Invalid sequence")