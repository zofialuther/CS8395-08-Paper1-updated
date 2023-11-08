def binary_search(l, value, low=0, high=-1):
    if not l:
        return -1
    if high == -1:
        high = len(l) - 1
    
    if high >= low:
        mid = (high + low) // 2
        if l[mid] == value:
            return mid
        elif l[mid] > value:
            return binary_search(l, value, low, mid-1)
        else:
            return binary_search(l, value, mid+1, high)
    else:
        return -1