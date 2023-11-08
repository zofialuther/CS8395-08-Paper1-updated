def selSort(xs):
    if len(xs) == 0:
        return []
    else:
        x = max(xs)
        xs.remove(x)
        return selSort(xs) + [x]