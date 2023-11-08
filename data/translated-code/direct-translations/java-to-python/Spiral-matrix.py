def main(args):
    print2dArray(getSpiralArray(5))

def getSpiralArray(dimension):
    spiralArray = [[0]*dimension for _ in range(dimension)]

    numConcentricSquares = int(math.ceil((dimension) / 2.0))

    sideLen = dimension
    currNum = 0

    for i in range(numConcentricSquares):
        # do top side
        for j in range(sideLen):
            spiralArray[i][i + j] = currNum
            currNum += 1

        # do right side
        for j in range(1, sideLen):
            spiralArray[i + j][dimension - 1 - i] = currNum
            currNum += 1

        # do bottom side
        for j in range(sideLen - 2, -1, -1):
            spiralArray[dimension - 1 - i][i + j] = currNum
            currNum += 1

        # do left side
        for j in range(sideLen - 2, 0, -1):
            spiralArray[i + j][i] = currNum
            currNum += 1

        sideLen -= 2

    return spiralArray

def print2dArray(array):
    for row in array:
        for elem in row:
            print("%3d" % elem, end="")
        print()

if __name__ == "__main__":
    main([])