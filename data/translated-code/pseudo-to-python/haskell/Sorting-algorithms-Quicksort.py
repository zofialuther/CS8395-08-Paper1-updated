def qsort(array):
    if not array:
        return []
    x = array[0]
    xs = array[1:]
    smaller = qsort([y for y in xs if y < x])
    larger = qsort([y for y in xs if y >= x])
    return smaller + [x] + larger