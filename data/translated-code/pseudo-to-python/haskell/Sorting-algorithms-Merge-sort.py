def mergeSort(xs):
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return xs
    else:
        (as, bs) = split(xs)
        return merge(mergeSort(as), mergeSort(bs))

def merge(xs, ys):
    if len(xs) == 0:
        return ys
    elif len(ys) == 0:
        return xs
    elif xs[0] <= ys[0]:
        return [xs[0]] + merge(xs[1:], ys)
    else:
        return [ys[0]] + merge(xs, ys[1:])

def split(xs):
    if len(xs) >= 2:
        (x, y, *zs) = xs
        (xs, ys) = split(zs)
        return ([x] + xs, [y] + ys)
    elif len(xs) == 1:
        return (xs, [])
    else:
        return ([], [])