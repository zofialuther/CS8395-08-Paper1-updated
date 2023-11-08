from typing import Tuple
import random
import numpy as np

def rand(range: Tuple[int, int], gen: np.random._generator.Generator) -> int:
    a = random.randint(range[0], range[1])
    return a

class Maze:
    def __init__(self, rightWalls: np.ndarray, belowWalls: np.ndarray):
        self.rightWalls = rightWalls
        self.belowWalls = belowWalls

def maze(width: int, height: int, gen: np.random._generator.Generator) -> Maze:
    visited = np.full((height, width), False)
    rWalls = np.full((height, width), True)
    bWalls = np.full((height, width), True)
    gen = gen
    x = rand((0, width - 1), gen)
    y = rand((0, height - 1), gen)
    visit(gen, visited, rWalls, bWalls, (x, y))
    return Maze(rWalls, bWalls)

def visit(gen: np.random._generator.Generator, visited: np.ndarray, rWalls: np.ndarray, bWalls: np.ndarray, here: Tuple[int, int]) -> None:
    visited[here] = True
    ns = neighbors(here)
    i = rand((0, len(ns) - 1), gen)
    for j, there in enumerate(ns):
        if j == i:
            continue
        seen = visited[there]
        if not seen:
            removeWall(here, there, rWalls, bWalls)
            visit(gen, visited, rWalls, bWalls, there)

def removeWall(here: Tuple[int, int], there: Tuple[int, int], rWalls: np.ndarray, bWalls: np.ndarray) -> None:
    x1, y1 = here
    x2, y2 = there
    if x1 == x2:
        if x1 > x2:
            rWalls[min(x1, x2), min(y1, y2)] = False
        else:
            rWalls[min(x1, x2), min(y1, y2)] = False
    else:
        if y1 > y2:
            bWalls[min(x1, x2), min(y1, y2)] = False
        else:
            bWalls[min(x1, x2), min(y1, y2)] = False

def neighbors(point: Tuple[int, int]) -> list:
    x, y = point
    ns = []
    if x > 0:
        ns.append((x-1, y))
    if x < maxX:
        ns.append((x+1, y))
    if y > 0:
        ns.append((x, y-1))
    if y < maxY:
        ns.append((x, y+1))
    return ns

def printMaze(maze: Maze) -> None:
    rWalls = maze.rightWalls
    bWalls = maze.belowWalls
    print('+' + ''.join(['---+' for _ in range(maxX + 1)]))
    for y in range(maxY + 1):
        print("|", end="")
        for x in range(maxX + 1):
            print("   ", end="")
            if rWalls[x, y]:
                print("|", end="")
            else:
                print(" ", end="")
        print("")
        for x in range(maxX + 1):
            print("+", end="")
            if bWalls[x, y]:
                print("   ", end="")
            else:
                print("---", end="")
        print("+")

maxX = 10
maxY = 7
gen = np.random.default_rng()
maze = maze(11, 8, gen)
printMaze(maze)