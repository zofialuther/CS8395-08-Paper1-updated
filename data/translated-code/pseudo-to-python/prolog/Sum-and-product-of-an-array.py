def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        head = arr[0]
        tail = arr[1:]
        y = sum(tail)
        return head + y

def product(arr):
    if len(arr) == 0:
        return 1
    else:
        head = arr[0]
        tail = arr[1:]
        y = product(tail)
        return head * y