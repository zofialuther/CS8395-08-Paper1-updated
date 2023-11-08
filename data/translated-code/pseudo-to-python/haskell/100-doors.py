def findIndices(array, condition):
    indices = []
    for i in range(len(array)):
        if condition(array[i]):
            indices.append(i)
    return indices

def toggleEvery(k, array):
    result = []
    cycleArray = [1, 0]
    cycleIndex = 0
    for i in range(len(array)):
        result.append(array[i] + cycleArray[cycleIndex])
        cycleIndex = (cycleIndex + 1) % k
    return result

def foldr(func, initialValue, array):
    result = initialValue
    for i in range(len(array) - 1, -1, -1):
        result = func(array[i], result)
    return result

def replicate(n, value):
    result = []
    for i in range(n):
        result.append(value)
    return result

def run(n):
    initialArray = replicate(n, 0)
    toggleFunc = lambda k, array: toggleEvery(k, array)
    foldedArray = foldr(toggleFunc, initialArray, list(range(n)))
    return findIndices(foldedArray, lambda num: num % 2 != 0)