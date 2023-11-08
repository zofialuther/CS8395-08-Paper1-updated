def flatten(lst):
    for x in lst:
        if isinstance(x, list):
            for y in flatten(x):
                yield y
        else:
            yield x

lst = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
print(list(flatten(lst)))