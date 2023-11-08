def quicksort(arr):
    if arr is None or len(arr) == 0:
        return []
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        equal = [x for x in arr[1:] if x == pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(equal) + quicksort(greater)