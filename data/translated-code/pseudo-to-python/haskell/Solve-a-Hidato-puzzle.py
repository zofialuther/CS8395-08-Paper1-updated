```python
nCells = 0
cMap = {}
best = None

def main(A):
    puzzle = showPuzzle("Input", readPuzzle())
    QMouse(puzzle, findStart(puzzle), None, 0)
    if solvePuzzle(puzzle):
        showPuzzle("Output", puzzle)
    else:
        print("No solution!")

def readPuzzle():
    p = [[-1]]
    maxCols = 0
    for line in input:
        p.append([-1] + list(gencells(line)) + [-1])
        maxCols = max(maxCols, len(p[-1]))
    p.append([-1])
    for i in range(1, len(p)):
        p[i] = p[i] + [-1] * (maxCols - len(p[i]))
    return p

def gencells(s):
    global nCells, cMap
    WS = " \t"
    NWS = "".join([c for c in string.printable if c not in WS])
    cMap = {}
    cMap["#"] = -1
    cMap["_"] = 0
    cMap[-1] = " "
    cMap[0] = "_"
    i = 0
    while i < len(s):
        w = (re.match(f"[{WS}]*", s[i:]).group(), re.match(f"[{NWS}]+", s[i:]).group())
        w = cMap[int(w[1])] if w[1] in cMap else int(w[1])
        if w != -1:
            nCells += 1
            yield w
        i += len(w[1])

def showPuzzle(label, p):
    print(label, " with ", nCells, " cells:")
    for r in p:
        for c in r:
            print(cMap[c] if c in cMap else c, end=" "*(nCells+1-len(str(cMap[c] if c in cMap else c)))
        print()
    return p

def findStart(p):
    if p[len(p) - 1][len(p[len(p) - 1]) - 1] == 1:
        return Pos(len(p) - 1, len(p[len(p) - 1]) - 1)

def solvePuzzle(puzzle):
    global best
    if path := best:
        while True:
            loc = path.getLoc()
            puzzle[loc.r][loc.c] = path.getVal()
            path = path.getParent()
            if not path:
                return puzzle
    else:
        return False

class Pos:
    def __init__(self, r, c):
        self.r = r
        self.c = c

class QMouse:
    def __init__(self, puzzle, loc, parent, val):
        self.puzzle = puzzle
        self.loc = loc
        self.parent = parent
        self.val = val

    def getVal(self):
        return self.val

    def getLoc(self):
        return self.loc

    def getParent(self):
        return self.parent

    def atEnd(self):
        return self.val == nCells == self.puzzle[self.loc.r][self.loc.c]

    def goNorth(self):
        return self.visit(self.loc.r - 1, self.loc.c)

    def goNE(self):
        return self.visit(self.loc.r - 1, self.loc.c + 1)

    def goEast(self):
        return self.visit(self.loc.r, self.loc.c + 1)

    # Rest of the methods here...

```