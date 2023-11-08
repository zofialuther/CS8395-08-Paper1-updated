import functools

def mapM_(func, lst):
    return functools.reduce(lambda x, y: func(y), lst)

def collect(lst):
    for item in lst:
        print(item)

# Example usage:
lst = [1, 2, 3, 4, 5]
mapM_(collect, lst)