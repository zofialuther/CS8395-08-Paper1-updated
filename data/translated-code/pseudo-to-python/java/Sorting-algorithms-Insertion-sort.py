def insertionSort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = abs(binarySearch(a, 0, i, x) + 1)
        a[j+1:i+1] = a[j:i]
        a[j] = x