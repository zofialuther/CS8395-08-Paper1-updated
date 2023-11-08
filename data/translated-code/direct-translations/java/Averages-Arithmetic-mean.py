def avg(*arr):
    sum = 0.0
    for x in arr:
        sum += x
    return sum / len(arr)