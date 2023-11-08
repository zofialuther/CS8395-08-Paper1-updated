def cocktailSort(l):
    swapped1 = True
    swapped2 = True
    while swapped1 or swapped2:
        swapped1 = False
        swapped2 = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped1 = True
        if not swapped1:
            return l
        for i in range(len(l)-2, -1, -1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped2 = True
        if not swapped2:
            return l
    return l

def swappingPass(op, pair, list):
    if len(list) > 1:
        if op(list[0], list[1]):
            return swappingPass(op, (True, list[1] + pair[1]), list[0] + list[2:])
        else:
            return swappingPass(op, pair, list[0] + list[1:])
    elif len(list) == 1:
        return (pair[0], (list[0] + pair[1]))
    else:
        return pair