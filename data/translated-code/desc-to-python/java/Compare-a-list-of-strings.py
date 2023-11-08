def allEqual(arr):
    first_string = arr[0]
    for string in arr:
        if string != first_string:
            return False
    return True