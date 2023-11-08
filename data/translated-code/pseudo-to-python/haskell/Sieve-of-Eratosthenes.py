```python
def primes():
    return [2] + Y(lambda s: [3] + gaps(5, U(lambda p: [p*p, p*p+2*p, ...]))

def Y(g):
    return g(lambda: Y(g))

def gaps(k, s):
    if k < s[0]:
        return [k] + gaps(k+2, s)
    else:
        return gaps(k+2, s[1:])

def U(arr):
    if len(arr) == 0:
        return []
    else:
        return [arr[0]] + merge(arr[1], U(arr[2:]))

def pairs(arr):
    if len(arr) < 2:
        return []
    else:
        return [merge(arr[0], arr[1])] + pairs(arr[2:])

def merge(xs, ys):
    if len(xs) == 0:
        return ys
    elif len(ys) == 0:
        return xs
    else:
        if xs[0] < ys[0]:
            return [xs[0]] + merge(xs[1:], ys)
        elif ys[0] < xs[0]:
            return [ys[0]] + merge(xs, ys[1:])
        else:
            return [xs[0]] + merge(xs[1:], ys[1:])
```