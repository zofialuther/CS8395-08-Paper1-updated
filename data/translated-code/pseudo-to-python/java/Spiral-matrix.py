def main():
    array = getSpiralArray(5)
    print2dArray(array)

def getSpiralArray(dimension):
    spiralArray = [[0 for i in range(dimension)] for j in range(dimension)]
    numConcentricSquares = -(-dimension // 2)
    sideLen = dimension
    currNum = 0

    for i in range(numConcentricSquares):
        for j in range(sideLen):
            spiralArray[i][i + j] = currNum
            currNum += 1

        for j in range(1, sideLen):
            spiralArray[i + j][dimension - 1 - i] = currNum
            currNum += 1

        for j in range(sideLen - 2, -1, -1):
            spiralArray[dimension - 1 - i][i + j] = currNum
            currNum += 1

        for j in range(sideLen - 2, 0, -1):
            spiralArray[i + j][i] = currNum
            currNum += 1

        sideLen -= 2

    return spiralArray

def print2dArray(array):
    for row in array:
        for element in row:
            print(f"{element:3}", end="")
        print()

main()