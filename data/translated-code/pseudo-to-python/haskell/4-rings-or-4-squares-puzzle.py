```python
def rings(u, digits):
    sortedDigits = sorted(digits, reverse=True)
    return queen(u, sortedDigits[0])

def queen(u, h, ds, q):
    ts = list(filter(lambda x: x <= h, ds))
    if u:
        xs = [x for x in ds if x not in [q]]
    else:
        xs = ds
    return [leftBishop(u, q, h, ts, ds, x) for x in xs]

def leftBishop(u, q, h, ts, ds, lb):
    lRook = lb + q
    if lRook <= h:
        if u:
            xs = [x for x in ts if x not in [q, lb, lRook]]
        else:
            xs = ds
        return [rightBishop(u, q, h, lb, ds, lRook, x) for x in xs]
    else:
        return []

def rightBishop(u, q, h, lb, ds, lRook, rb):
    rRook = q + rb
    if rRook <= h and (not u or rRook != lb):
        ks = [x for x in ds if x not in [q, lb, rb, rRook, lRook]] if u else ds
        return [knights(u, lRook - rRook, lRook, lb, q, rb, rRook, ks, k) for k in ks]
    else:
        return []

def knights(u, rookDelta, lRook, lb, q, rb, rRook, ks, k):
    k2 = k + rookDelta
    return [(lRook, k, lb, q, rb, k2, rRook) for k2 in ks if (not u or k2 not in [lRook, k, lb, q, rb, rRook])]

def main():
    f = lambda k, xs: print(k) and nl() and list(map(print, xs)) and nl()
    nl = lambda: print([])
    list(map(f, [("rings True [1 .. 7]", rings(True, [1, 2, 3, 4, 5, 6, 7])), ("rings True [3 .. 9]", rings(True, [3, 4, 5, 6, 7, 8, 9]))]))
    f("length(rings False [0 .. 9])", [len(rings(False, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))])

main()
```