```python
from typing import List
from functools import reduce
from operator import add

Square = (int, int)

def knightTour(moves: List[Square]) -> List[Square]:
    if not moves:
        return moves[::-1]
    else:
        possibilities = findMoves(moves[0])
        newSquare = min(possibilities, key=lambda s: len(findMoves(s)))
        return knightTour([newSquare] + moves)

def findMoves(square: Square) -> List[Square]:
    return list(set(knightOptions(square)).difference(set([square])))

def knightOptions(square: Square) -> List[Square]:
    x = square[0]
    y = square[1]
    return reduce(add, map(go, [(x+i, y+j) for i in [1, 2, -1, -2] for j in [1, 2, -1, -2] if abs(i) != abs(j) and onBoard(x+i) and onBoard(y+j)]))

def go(square: Square) -> List[Square]:
    if both(onBoard, square):
        return [square]
    else:
        return []

def knightMoves() -> List[Square]:
    return [move for move in [(i, x) for i in [1, 2, -1, -2] for x in [1, 2, -1, -2] if abs(i) != abs(x)]]

def onBoard(num: int) -> bool:
    return 1 <= num <= 8

def both(func, pair):
    return join(bimap(func, pair))

def startPoint() -> str:
    return "e5"

def algebraic(coords: Square) -> str:
    x = coords[0]
    y = coords[1]
    return chr(x + 96) + chr(y + 48)

def main() -> None:
    startPoint = "e5"
    tour = [algebraic(coord) for coord in knightTour([((ord(startPoint[0]) - 96), (ord(startPoint[1]) - 48))])]
    if not tour:
        return
    else:
        printTour(tour)

def printTour(tour: List[str]) -> None:
    if not tour:
        return
    else:
        print(' -> '.join(tour[:8]))
        printTour(tour[8:])
```