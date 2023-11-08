ludic = 1:2 : f 3 [3..] [(4,2)] 
def f(n, xs, yy):
    i, y = yy[0]
    if n == i:
        return f(n, dropEvery(y, xs), yy[1:])
    else:
        return [xs[0]] + f(1+n, xs[1:], yy + [(n+xs[0], xs[0])])

def dropEvery(n, s):
    a, b = s[0:n-1], s[n:]
    return a + dropEvery(n, b[1:]) if len(b) > 0 else a

print(ludic[10000 - 1])