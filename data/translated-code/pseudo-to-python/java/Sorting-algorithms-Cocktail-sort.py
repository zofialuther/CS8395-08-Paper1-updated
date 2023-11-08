def cocktailSort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
                swapped = True