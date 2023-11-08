def f(n, xs, yy):
    if n == yy[0][0]:
        return f(n, dropEvery(yy[0][1], xs), yy[1:])
    else:
        return [xs[0]] + f(1+n, xs[1:], yy + [(n+xs[0], xs[0])])

def dropEvery(n, s):
    a, b = s[:n-1], s[n:]
    return a + dropEvery(n, b) if len(b) > 0 else a

ludic = f(3, [i for i in range(3, 1000)], [(4, 2)])
print(ludic[9999])