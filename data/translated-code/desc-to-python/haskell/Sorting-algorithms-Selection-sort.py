def selSort(arr):
    if len(arr) == 0:
        return []
    else:
        max_element = max(arr)
        arr.remove(max_element)
        return selSort(arr) + [max_element]