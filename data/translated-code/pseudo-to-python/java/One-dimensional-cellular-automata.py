class Life:
    def main(self):
        start = "_###_##_#_#_#_#__#__"
        numGens = 10
        for i in range(numGens):
            print("Generation " + str(i) + ": " + start)
            start = self.life(start)

    def life(self, lastGen):
        newGen = ""
        for i in range(len(lastGen)):
            neighbors = 0
            if i == 0:
                neighbors = 1 if lastGen[1] == '#' else 0
            elif i == len(lastGen) - 1:
                neighbors = 1 if lastGen[i - 1] == '#' else 0
            else:
                neighbors = self.getNeighbors(lastGen[i - 1:i + 2])
            if neighbors == 0:
                newGen += "_"
            if neighbors == 1:
                newGen += lastGen[i]
            if neighbors == 2:
                newGen += "_" if lastGen[i] == '#' else "#"
        return newGen

    def getNeighbors(self, group):
        ans = 0
        if group[0] == '#':
            ans += 1
        if group[2] == '#':
            ans += 1
        return ans