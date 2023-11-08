```python
nCells = 0
cMap = {}
best = None

class Pos:
    def __init__(self, r, c):
        self.r = r
        self.c = c

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
    for line in iter(input, ''):
        p.append([-1] + gencells(line) + [-1])
        maxCols = max(maxCols, len(p[-1]))
    p.append([-1])
    for i in range(1, len(p)):
        p[i] = p[i] + [-1] * (maxCols - len(p[i]))
    return p

def gencells(s):
    global nCells, cMap
    if not cMap:
        cMap = {"#": -1, "_": 0, -1: " ", 0: "_"}
    result = []
    for word in s.split():
        w = cMap.get(word, word)
        if w != -1:
            nCells += 1
        result.append(w)
    return result

def showPuzzle(label, p):
    print(label, " with ", nCells, " cells:")
    for r in p:
        for c in r:
            print(str(cMap.get(c, c)).rjust(nCells + 1), end='')
        print()
    return p

def findStart(p):
    r = 0
    c = 0
    if p[r][c] == 1:
        return Pos(r, c)

def solvePuzzle(puzzle):
    global best
    if best:
        path = best
        while path:
            loc = path.getLoc()
            puzzle[loc.r][loc.c] = path.getVal()
            path = path.getParent()
        return puzzle

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
        return self.puzzle[self.loc.r][self.loc.c] == self.val

    def visit(self, r, c):
        if not best and self.validPos(r, c):
            return Pos(r, c)

    def validPos(self, r, c):
        xv = self.puzzle[r][c]
        if xv == (self.val + 1):
            return True
        if xv == 0:
            ancestor = self
            while xl := (ancestor := ancestor.getParent()).getLoc():
                if xl.r == r and xl.c == c:
                    return False
            return True

    def goNorth(self):
        return self.visit(self.loc.r - 1, self.loc.c)

    def goNE(self):
        return self.visit(self.loc.r - 1, self.loc.c + 1)

    def goEast(self):
        return self.visit(self.loc.r, self.loc.c + 1)

    def goSE(self):
        return self.visit(self.loc.r + 1, self.loc.c + 1)

    def goSouth(self):
        return self.visit(self.loc.r + 1, self.loc.c)

    def goSW(self):
        return self.visit(self.loc.r + 1, self.loc.c - 1)

    def goWest(self):
        return self.visit(self.loc.r, self.loc.c - 1)

    def goNW(self):
        return self.visit(self.loc.r - 1, self.loc.c - 1)

    def initially(self):
        self.val += 1
        if self.atEnd():
            global best
            best = self
            return
        QMouse(self.puzzle, self.goNorth(), self, self.val)
        QMouse(self.puzzle, self.goNE(), self, self.val)
        QMouse(self.puzzle, self.goEast(), self, self.val)
        QMouse(self.puzzle, self.goSE(), self, self.val)
        QMouse(self.puzzle, self.goSouth(), self, self.val)
        QMouse(self.puzzle, self.goSW(), self, self.val)
        QMouse(self.puzzle, self.goWest(), self, self.val)
        QMouse(self.puzzle, self.goNW(), self, self.val)

main("A")
```