```python
import random

baseSize = 12
actualBoardSize = baseSize - 4
moves = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
grid = []
totalNodes = 0
travelledNodes = []

def KT(baseNumber):
    global baseSize, actualBoardSize
    baseSize = baseNumber
    actualBoardSize = baseSize - 4

def main():
    kt1 = KT(12)
    kt1.tour()

    kt2 = KT(24)
    kt2.tour()

    kt3 = KT(104)
    kt3.tour()

def tour():
    global totalNodes, travelledNodes, grid
    totalNodes = actualBoardSize * actualBoardSize
    travelledNodes.clear()
    grid = [[0 for _ in range(baseSize)] for _ in range(baseSize)]
    startRow = random.randint(2, actualBoardSize + 1)
    startCol = random.randint(2, actualBoardSize + 1)
    start = [startRow, startCol, 0, 1]
    grid[startRow][startCol] = 1
    travelledNodes.append(start)
    autoKnightTour(start, 2)

def autoKnightTour(start, nextCount):
    global totalNodes, travelledNodes, grid
    nbrs = neighbors(start[0], start[1])
    if nbrs:
        nbrs.sort(key=lambda x: countNeighbors(x[0], x[1]))
        next = nbrs[0]
        next[3] = nextCount
        travelledNodes.append(next)
        grid[next[0]][next[1]] = nextCount
        if len(travelledNodes) == totalNodes:
            print(f"Found a path for {actualBoardSize} X {actualBoardSize} chess board")
            sb = ""
            for index, item in enumerate(travelledNodes):
                sb += f" -> ({item[0] - 2},{item[1] - 2})"
                if (index + 1) % 15 == 0:
                    sb += "\n"
            print(sb)
        else:
            autoKnightTour(next, nextCount + 1)
    else:
        last = travelledNodes[-1]
        travelledNodes = reChain(travelledNodes)
        if travelledNodes[-1] == last:
            travelledNodes = reChain(travelledNodes)
            if travelledNodes[-1] == last:
                print("Re-chained twice but no travllable node found. Quiting...")
            else:
                end = travelledNodes[-1]
                autoKnightTour(end, nextCount)
        else:
            end = travelledNodes[-1]
            autoKnightTour(end, nextCount)

def reChain(alreadyTraveled):
    last = alreadyTraveled[-1]
    candidates = neighborsInChain(last[0], last[1])
    randomPicked = random.choice(candidates)
    cutIndex = grid[randomPicked[0]][randomPicked[1]] - 1
    result = []
    for k in range(cutIndex):
        result.append(alreadyTraveled[k])
    for j in range(len(alreadyTraveled) - 1, cutIndex, -1):
        alreadyTraveled[j][3] = len(result)
        result.append(alreadyTraveled[j])
    return result

def neighborsInChain(r, c):
    nbrs = []
    for move in moves:
        x = move[0]
        y = move[1]
        if grid[r + y][c + x] > 0 and grid[r + y][c + x] != grid[r][c] - 1:
            num = countNeighbors(r + y, c + x)
            nbrs.append([r + y, c + x, num, 0])
    return nbrs

def neighbors(r, c):
    nbrs = []
    for move in moves:
        x = move[0]
        y = move[1]
        if grid[r + y][c + x] == 0:
            num = countNeighbors(r + y, c + x)
            nbrs.append([r + y, c + x, num, 0])
    return nbrs

def countNeighbors(r, c):
    num = 0
    for move in moves:
        if grid[r + move[1]][c + move[0]] == 0:
            num += 1
    return num
```