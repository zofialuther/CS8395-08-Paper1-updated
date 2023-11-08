def mean(lst):
    if not lst:
        return 0
    else:
        total = 0
        for value in lst:
            total = total + value
        mean = total / len(lst)
        return mean