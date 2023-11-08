def equlibrium_indices(sequence):
    totalSum = sum(sequence)
    runningSum = 0
    for i in range(len(sequence)):
        n = sequence[i]
        if totalSum - runningSum - n == runningSum:
            print(i)
        runningSum += n

sequence = [-7, 1, 5, 2, -4, 3, 0]
equlibrium_indices(sequence)