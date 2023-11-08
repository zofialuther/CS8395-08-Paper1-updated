def plusplus(lst, x):
    if not lst:
        return x
    else:
        return [lst[0]] + plusplus(lst[1:], x)