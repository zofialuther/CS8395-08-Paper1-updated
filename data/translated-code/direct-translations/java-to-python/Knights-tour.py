```python
import random

class KT:

    def __init__(self, baseNumber):
        self.baseSize = baseNumber
        self.actualBoardSize = self.baseSize - 4

    def main(self):
        self.tour()  # find a solution for 8X8 board
#        self.tour()  # then for 20X20 board
#        self.tour()  # then for 100X100 board

    def tour(self):
        totalNodes = self.actualBoardSize * self.actualBoardSize
        self.travelledNodes = []
        grid = [[0 for _ in range(self.baseSize)] for _ in range(self.baseSize)]
        for r in range(self.baseSize):
            for c in range(self.baseSize):
                if r < 2 or r > self.baseSize - 3 or c < 2 or c > self.baseSize - 3:
                    grid[r][c] = -1  # mark as out-of-board nodes
                else:
                    grid[r][c] = 0  # nodes within chess board.

        startRow = 2 + random.randint(0, self.actualBoardSize - 1)
        startCol = 2 + random.randint(0, self.actualBoardSize - 1)
        start = [startRow, startCol, 0, 1]
        grid[startRow][startCol] = 1  # mark the first traveled node
        self.travelledNodes.append(start)  # add to partial solution chain, which will only have one node.

        self.autoKnightTour(start, 2)

    def autoKnightTour(self, start, nextCount):
        nbrs = self.neighbors(start[0], start[1])
        if len(nbrs) > 0:
            nbrs.sort(key=lambda x: x[2])
            next = nbrs[0]
            next[3] = nextCount
            self.travelledNodes.append(next)
            grid[next[0]][next[1]] = nextCount
            if len(self.travelledNodes) == totalNodes:
                print(f"Found a path for {self.actualBoardSize} X {self.actualBoardSize} chess board.")
                sb = []
                for idx, item in enumerate(self.travelledNodes):
                    sb.append(f"->({item[0] - 2},{item[1] - 2})")
                    if (idx + 1) % 15 == 0:
                        sb.append("\n")
                print(''.join(sb) + "\n")
            else:
                self.autoKnightTour(next, nextCount + 1)
        else:
            last = self.travelledNodes[-1]
            self.travelledNodes = self.reChain(self.travelledNodes)
            if self.travelledNodes[-1] == last:
                self.travelledNodes = self.reChain(self.travelledNodes)
                if self.travelledNodes[-1] == last:
                    print("Re-chained twice but no travllable node found. Quiting...")
                else:
                    end = self.travelledNodes[-1]
                    self.autoKnightTour(end, nextCount)
            else:
                end = self.travelledNodes[-1]
                self.autoKnightTour(end, nextCount)

    def reChain(self, alreadyTraveled):
        last = alreadyTraveled[-1]
        candidates = self.neighborsInChain(last[0], last[1])
        randomPicked = candidates[random.randint(0, len(candidates) - 1)]
        cutIndex = grid[randomPicked[0]][randomPicked[1]] - 1
        result = []
        for k in range(cutIndex + 1):
            result.append(alreadyTraveled[k])
        for j in range(len(alreadyTraveled) - 1, cutIndex, -1):
            alreadyTraveled[j][3] = len(result)
            result.append(alreadyTraveled[j])
        return result

    def neighborsInChain(self, r, c):
        nbrs = []
        for m in moves:
            x, y = m
            if grid[r + y][c + x] > 0 and grid[r + y][c + x] != grid[r][c] - 1:
                num = self.countNeighbors(r + y, c + x)
                nbrs.append([r + y, c + x, num, 0])
        return nbrs

    def neighbors(self, r, c):
        nbrs = []
        for m in moves:
            x, y = m
            if grid[r + y][c + x] == 0:
                num = self.countNeighbors(r + y, c + x)
                nbrs.append([r + y, c + x, num, 0])  # not-traveled neighbors and number of their neighbors
        return nbrs

    def extendableNeighbors(self, neighbors):
        nbrs = []
        for node in neighbors:
            if node[2] > 0:
                nbrs.append(node)
        return nbrs

    def countNeighbors(self, r, c):
        num = 0
        for m in moves:
            if grid[r + m[1]][c + m[0]] == 0:
                num += 1
        return num


moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

KT(12).main()
```