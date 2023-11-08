def qsort(lst):
    if not lst:
        return lst
    else:
        pivot = lst[0]
        lesser = qsort([x for x in lst[1:] if x < pivot])
        greater = qsort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater