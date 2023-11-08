```python
from control.applicative import (<|>)
import control.monad
import control.monad.csp
from data.list import transpose
import system.environment (getArgs)
from text.parsercombinators.readp import ReadP
import qualified text.parsercombinators.readp as P
from text.printf import printf

def main():
    file = parseArgs()
    printf("reading problem file from %s\n" % file)
    ps = parseProblems(file)
    for p in ps:
        print(p)
        print("")
        printSolution(solve(p))
        print("")

# parsing
def parseArgs():
    args = getArgs()
    if len(args) == 1:
        return args[0]
    else:
        raise ValueError("expected exactly one command line argument, the name of the problem file")

class Problem:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return f"Problem(rows={self.rows}, cols={self.cols})"

def entryP():
    n = ord(P.get())
    if n < 65 or n > 90:
        P.pfail()
    return n - 64

def blankP(), eolP():
    return P.char(' '), P.char('\n')

def entriesP():
    return ([] <|> blankP()) or P.many1(entryP())

def lineP():
    return P.sepBy1(entriesP(), blankP()) or eolP()

def problemP():
    return Problem(lineP(), lineP())

def problemsP():
    return P.sepBy1(problemP(), P.many(blankP()) or eolP()) or P.eof()

def parseProblems(file):
    s = readFile(file)
    ps, _ = P.readP_to_S(problemsP(), s)
    return ps

# CSP
def solve(p):
    return oneCSPSolution(problemCSP(p))

def problemCSP(p):
    rowCount = len(p.rows)
    colCount = len(p.cols)
    cells = [[mkDV([False, True]) for _ in range(colCount)] for _ in range(rowCount)]

    for ws, r in zip(cells, p.rows):
        rowOrColCSP(ws, r)
    for ws, c in zip(transpose(cells), p.cols):
        rowOrColCSP(ws, c)

    return cells

def rowOrColCSP(ws, xs):
    if not xs:
        for w in ws:
            constraint1(not, w)
    else:
        vs = list(enumerate(ws))
        n = len(ws)

        blocks = [mkDV([(i, i + x - 1) for i in range(n - x + 1)]) for x in xs]

        f(blocks)

        for x in blocks:
            for i, y in vs:
                constraint2(lambda (x1, x2), b: i < x1 or i > x2 or b, x, y)

        for i, y in vs:
            constraint2(lambda (y', _), b: i >= y' or not b, blocks[0], y)

        for i, y in vs:
            constraint2(lambda (_, y'), b: i <= y' or not b, blocks[-1], y)

        for x, y in zip(blocks, blocks[1:]):
            for i, z in vs:
                constraint3(lambda (_, x'), (y', _), b: i <= x' or i >= y' or not b, x, y, z)

def f(blocks):
    if len(blocks) >= 2:
        constraint2(lambda (_, u'), (v', _): v' >= u' + 2, blocks[0], blocks[1])
        f(blocks[1:])

# printing
def printSolution(bss):
    for bs in bss:
        for b in bs:
            print('#' if b else '.', end="")
        print("")
```