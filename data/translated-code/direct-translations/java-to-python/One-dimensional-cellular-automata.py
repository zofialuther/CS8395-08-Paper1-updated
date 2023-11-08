```python
class Life:
    @staticmethod
    def main(args):
        start = "_###_##_#_#_#_#__#__"
        numGens = 10
        for i in range(numGens):
            print("Generation " + str(i) + ": " + start)
            start = Life.life(start)

    @staticmethod
    def life(lastGen):
        newGen = ""
        for i in range(len(lastGen)):
            neighbors = 0
            if i == 0:  # left edge
                neighbors = 1 if lastGen[1] == '#' else 0
            elif i == len(lastGen) - 1:  # right edge
                neighbors = 1 if lastGen[i - 1] == '#' else 0
            else:  # middle
                neighbors = Life.getNeighbors(lastGen[i - 1:i + 2])

            if neighbors == 0:  # dies or stays dead with no neighbors
                newGen += "_"
            if neighbors == 1:  # stays with one neighbor
                newGen += lastGen[i]
            if neighbors == 2:  # flips with two neighbors
                newGen += "_" if lastGen[i] == '#' else "#"
        return newGen

    @staticmethod
    def getNeighbors(group):
        ans = 0
        if group[0] == '#':
            ans += 1
        if group[2] == '#':
            ans += 1
        return ans


Life.main([])
```