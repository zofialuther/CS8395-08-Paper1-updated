def sum(lst):
    if not lst:
        return 0
    return lst[0] + sum(lst[1:])

def product(lst):
    if not lst:
        return 1
    return lst[0] * product(lst[1:])