def getHailstoneSequence(n):
    if n <= 0:
        raise ValueError("Invalid starting sequence number")
    sequence = [n]
    while n != 1:
        if n & 1 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    sequence27 = getHailstoneSequence(27)
    print("Sequence for 27 has " + str(len(sequence27)) + " elements:", sequence27)

    MAX = 100000
    highestNumber1 = 1
    highestCount1 = 1
    for i in range(2, MAX):
        count = len(getHailstoneSequence(i))
        if count > highestCount1:
            highestCount1 = count
            highestNumber1 = i
    print("Method 1, number " + str(highestNumber1) + " has the longest sequence, with a length of " + str(highestCount1))

    highestNumber2 = 1
    highestCount2 = 1
    for i in range(2, MAX):
        count = 1
        n = i
        while n != 1:
            if n & 1 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            count = count + 1
        if count > highestCount2:
            highestCount2 = count
            highestNumber2 = i
    print("Method 2, number " + str(highestNumber2) + " has the longest sequence, with a length of " + str(highestCount2))

    highestNumber3 = 1
    highestCount3 = 1
    sequenceMap = {1: 1}
    for i in range(2, MAX):
        currentList = []
        n = i
        count = sequenceMap.get(n)
        while count is None:
            currentList.append(n)
            if n & 1 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            count = sequenceMap.get(n)
        curCount = count
        for j in range(len(currentList) - 1, -1, -1):
            sequenceMap[currentList[j]] = curCount + 1
            curCount = curCount + 1
        if curCount > highestCount3:
            highestCount3 = curCount
            highestNumber3 = i
    print("Method 3, number " + str(highestNumber3) + " has the longest sequence, with a length of " + str(highestCount3))