def insertionSort(arr):
    def insert(x, xs):
        return [y for y in xs if y < x] + [x] + [y for y in xs if y >= x]

    return functools.reduce(insert, arr, [])