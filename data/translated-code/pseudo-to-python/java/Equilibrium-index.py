sequence = [-7, 1, 5, 2, -4, 3, 0]

def equlibrium_indices(sequence):
    totalSum = 0
    for n in sequence:
        totalSum += n
    
    runningSum = 0
    for i in range(len(sequence)):
        n = sequence[i]
        if totalSum - runningSum - n == runningSum:
            print(i)
        runningSum += n

equlibrium_indices(sequence)