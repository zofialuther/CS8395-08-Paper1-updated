def qsort(arr):
    if not arr:
        return []
    else:
        x = arr[0]
        xs = arr[1:]
        return qsort([y for y in xs if y < x]) + [x] + qsort([y for y in xs if y >= x])