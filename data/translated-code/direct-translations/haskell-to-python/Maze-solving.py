```python
import sys
from typing import List, Tuple, Optional

# given two points, returns the average of them
def average(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    x = (p1[0] + p2[0]) // 2
    y = (p1[1] + p2[1]) // 2
    return (x, y)

# given a maze and a tuple of position and wall position, returns
# true if the wall position is not blocked (first position is unused)
def notBlocked(maze: List[str], positions: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
    unused, wall_pos = positions
    x, y = wall_pos
    return maze[y][x] == ' '

# given a list, a position, and an element, returns a new list
# with the new element substituted at the position
def substitute(orig: List, pos: int, el: any) -> List:
    before = orig[:pos]
    after = orig[pos+1:]
    return before + [el] + after

# given a maze and a position, draw a '*' at that position in the maze
def draw(maze: List[str], position: Tuple[int, int]) -> List[str]:
    x, y = position
    row = maze[y]
    new_row = substitute(row, x, '*')
    new_maze = maze[:y] + [new_row] + maze[y+1:]
    return new_maze

# given a maze, a previous position, and a list of tuples of potential
# new positions and their wall positions, returns the solved maze, or
# None if it cannot be solved
def tryMoves(maze: List[str], prevPos: Tuple[int, int], positions: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> Optional[List[str]]:
    if not positions:
        return None
    new_pos, wall_pos = positions[0]
    result = solve_(maze, new_pos, prevPos)
    if result is None:
        return tryMoves(maze, prevPos, positions[1:])
    else:
        new_maze = result
        for pos in [new_pos, wall_pos]:
            new_maze = draw(new_maze, pos)
        return new_maze

# given a maze, a new position, and a previous position, returns
# the solved maze, or None if it cannot be solved
# (assumes goal is upper-left corner of maze)
def solve_(maze: List[str], pos: Tuple[int, int], prevPos: Tuple[int, int]) -> Optional[List[str]]:
    if pos == (2, 1):
        return maze
    x, y = pos
    new_positions = [(x, y - 2), (x + 4, y), (x, y + 2), (x - 4, y)]
    new_positions_ = [p for p in new_positions if p != prevPos]
    wall_positions = [average(pos, p) for p in new_positions_]
    zipped = list(zip(new_positions_, wall_positions))
    legal_moves = [p for p in zipped if notBlocked(maze, p)]
    return tryMoves(maze, pos, legal_moves)

# given a maze, returns a solved maze, or None if it cannot be solved
# (starts at lower right corner and goes to upper left corner)
def solve(maze: List[str]) -> Optional[List[str]]:
    startx = len(maze[0]) - 3
    starty = len(maze) - 2
    start = (startx, starty)
    return solve_(draw(maze, start), start, (-1, -1))

# takes unsolved maze on standard input, prints solved maze on standard output
def main():
    input_maze = sys.stdin.read().splitlines()
    solved_maze = solve(input_maze)
    if solved_maze is not None:
        for row in solved_maze:
            print(row)
    else:
        print("can't solve")

if __name__ == "__main__":
    main()
```