def median(values):
    list = values.copy()
    list.sort()
    mid = len(list) // 2
    if len(list) % 2 == 0:
        valueA = list[mid]
        valueB = list[mid + 1]
        return (valueA + valueB) / 2
    elif len(list) % 2 == 1:
        return list[mid]
    else:
        return 0