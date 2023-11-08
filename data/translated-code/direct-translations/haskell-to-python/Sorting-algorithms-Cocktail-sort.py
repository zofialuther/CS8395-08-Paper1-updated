def cocktailSort(l):
    def swappingPass(op, pair, lst):
        swapped, l = pair
        if len(lst) >= 2:
            x1, x2, *xs = lst
            if op(x1, x2):
                return swappingPass(op, (True, [x2] + l), [x1] + xs)
            else:
                return swappingPass(op, (swapped, [x1] + l), [x2] + xs)
        elif len(lst) == 1:
            x = lst[0]
            return (swapped, [x] + l)
        else:
            return pair

    swapped1, l1 = swappingPass(lambda a, b: a > b, (False, []), l)
    swapped2, l2 = swappingPass(lambda a, b: a < b, (False, []), l1)

    if not swapped1:
        return l
    elif not swapped2:
        return list(reversed(l1))
    else:
        return cocktailSort(l2)