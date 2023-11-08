```python
import sys

def read_lines(f):
    lines = []
    for line in f:
        lines.append(line.rstrip())
    return lines

def decimate_horizontally(lines):
    width = (len(lines[0]) + 1) // 2
    c = []
    for line in lines:
        new_line = []
        for j in range(0, width):
            new_line.append(line[j*2])
        c.append(new_line)
    return c

def solve_maze_recursively(maze, x, y, d):
    ok = False
    directions = [(0, -1, 2), (1, 0, 3), (0, 1, 0), (-1, 0, 1)]
    for i in range(4):
        if i != d:
            dx, dy, opposite_d = directions[i]
            if maze[y+dy][x+dx] == ' ':
                ok = solve_maze_recursively(maze, x + (dx*2), y + (dy*2), opposite_d)
            if ok:
                break
    if x == 1 and y == 1:
        ok = True
    if ok:
        maze[y][x] = '*'
        dx, dy, _ = directions[d]
        maze[y+dy][x+dx] = '*'
    return ok

def solve_maze(maze):
    solve_maze_recursively(maze, len(maze[0]) - 2, len(maze) - 2, -1)

def expand_horizontally(maze):
    lines = []
    for row in maze:
        new_line = ""
        for cell in row:
            new_line += cell
            new_line += cell if cell != ' ' else ' '
        lines.append(new_line)
    return lines

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = read_lines(f)
    else:
        lines = read_lines(sys.stdin)
    maze = decimate_horizontally(lines)
    solve_maze(maze)
    solved_lines = expand_horizontally(maze)
    for line in solved_lines:
        print(line)

if __name__ == "__main__":
    main()
```