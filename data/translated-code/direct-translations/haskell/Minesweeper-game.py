```python
from typing import List, Tuple
import random
from dataclasses import dataclass

Pos = Tuple[int, int]
CellState = Covered | UnCovered

@dataclass
class Covered:
    mined: bool
    flagged: bool

@dataclass
class UnCovered:
    mined: bool

@dataclass
class Cell:
    pos: Pos
    state: CellState
    cellId: int
    adjacentMines: int

from typing import List, Tuple
import random
from dataclasses import dataclass

Pos = Tuple[int, int]
CellState = Covered | UnCovered

@dataclass
class Covered:
    mined: bool
    flagged: bool

@dataclass
class UnCovered:
    mined: bool

@dataclass
class Cell:
    pos: Pos
    state: CellState
    cellId: int
    adjacentMines: int

def coveredLens(cell):
    return (cell.state.mined, cell.state.flagged)

def coveredMinedLens(cell):
    return cell.state.mined

def coveredFlaggedLens(cell):
    return cell.state.flagged

def xCoordLens(cell):
    return cell.pos[0]

def yCoordLens(cell):
    return cell.pos[1]

totalRows = 4
totalCols = 6

emptyBoard = [Cell(pos=(x, y), state=Covered(False, False), adjacentMines=0, cellId=n) for n, (x, y) in enumerate([(x, y) for x in range(1, totalCols + 1) for y in range(1, totalRows + 1)])]

def updateCell(cell, board):
    return [cell if cell.cellId == c.cellId else c for c in board]

def updateBoard(board, cells):
    return [updateCell(cell, board) for cell in cells]

def okToOpen(cells):
    return [c for c in cells if not coveredLens(c) == (False, False)]

def openUnMined(cell):
    return Cell(pos=cell.pos, state=UnCovered(False), cellId=cell.cellId, adjacentMines=cell.adjacentMines)

def openCell(pos, board):
    cell = next((c for c in board if c.pos == pos), None)
    if cell:
        if cell.state.flagged:
            return board
        elif cell.state.mined:
            return updateCell(openUnMined(cell), board)
        elif isCovered(cell):
            if cell.adjacentMines == 0 and not isFirstMove(board):
                return updateCell(openUnMined(cell), expandEmptyCells(board, cell))
            else:
                return updateCell(openUnMined(cell), board)
        else:
            return board
    else:
        return board

def expandEmptyCells(board, cell):
    openedCells = [openUnMined(c) for c in nub(findMore([cell], adjacent(cell, board))) if c.adjacentMines == 0]
    return updateBoard(board, openedCells)

def flagCell(pos, board):
    cell = next((c for c in board if c.pos == pos), None)
    if cell:
        return updateCell(cell._replace(state=cell.state._replace(flagged=not cell.state.flagged)), board)
    else:
        return board

def adjacentCells(cell, board):
    x, y = cell.pos
    positions = [(x1, y1) for x1 in range(x-1, x+2) for y1 in range(y-1, y+2) if 0 < x1 <= totalCols and 0 < y1 <= totalRows and (x1, y1) != (x, y)]
    return [c for c in board if c.pos in positions]

def isLoss(board):
    return any(c.state.mined for c in board if c.state.uncovered)

def isWin(board):
    return allUnMinedOpen(board) or allMinesFlagged(board)

def allUnMinedOpen(board):
    return len([c for c in board if not c.state.mined and not c.state.uncovered]) == 0

def allMinesFlagged(board):
    minedCount = len([c for c in board if c.state.mined and c.state.flagged])
    flaggedMineCount = len([c for c in board if c.state.mined and c.state.flagged])
    return minedCount == flaggedMineCount

def isFirstMove(board):
    return len([c for c in board if not c.state.flagged]) == totalCols * totalRows

def groupedByRows(board):
    return [sorted(g, key=lambda c: c.pos[1]) for k, g in groupby(sorted(board, key=lambda c: c.pos[1]), lambda c: c.pos[1])]

def displayCell(cell):
    if cell.state.uncovered:
        return "X"
    elif cell.state.flagged:
        return "?"
    elif not cell.state.uncovered:
        if cell.adjacentMines > 0:
            return str(cell.adjacentMines)
        else:
            return "▢"
    else:
        return "."

def exposeMines(board):
    return [c._replace(state=UnCovered(True)) for c in board if c.state.mined]

def updateMineCount(board):
    return [c._replace(adjacentMines=sum(1 for c in adjacentCells(c, board) if c.state.mined)) for c in board]

def mineBoard(pos, board):
    totalMines = randomMinedCount()
    mined = random.sample(range(1, totalCols * totalRows + 1), totalMines)
    minedBoard = [c._replace(state=c.state._replace(mined=True)) for c in board if c.cellId in mined]
    return updateMineCount(minedBoard)

def randomMinedCount():
    return random.randint(minMinedCells(), maxMinedCells())

def minMinedCells():
    return int(totalCols * totalRows * 0.1)

def maxMinedCells():
    return int(totalCols * totalRows * 0.2)
```