```python
def readLines(f):
    r = BufferedReader(InputStreamReader(f, "US-ASCII"))
    lines = ArrayList()
    line = ""
    while line = r.readLine() is not None:
        lines.add(line)
    return lines.toArray(new String[0])

def decimateHorizontally(lines):
    width = (len(lines[0]) + 1) // 2
    c = [[0 for j in range(width)] for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(width):
            c[i][j] = lines[i][j * 2]
    return c

def solveMazeRecursively(maze, x, y, d):
    ok = False
    for i in range(4) and not ok:
        if i != d:
            if i == 0:
                if maze[y-1][x] == ' ':
                    ok = solveMazeRecursively(maze, x, y - 2, 2)
            elif i == 1:
                if maze[y][x+1] == ' ':
                    ok = solveMazeRecursively(maze, x + 2, y, 3)
            elif i == 2:
                if maze[y+1][x] == ' ':
                    ok = solveMazeRecursively(maze, x, y + 2, 0)
            elif i == 3:
                if maze[y][x-1] == ' ':
                    ok = solveMazeRecursively(maze, x - 2, y, 1)
    if x == 1 and y == 1:
        ok = True
    if ok:
        maze[y][x] = '*'
        if d == 0:
            maze[y-1][x] = '*'
        elif d == 1:
            maze[y][x+1] = '*'
        elif d == 2:
            maze[y+1][x] = '*'
        elif d == 3:
            maze[y][x-1] = '*'
    return ok

def solveMaze(maze):
    solveMazeRecursively(maze, len(maze[0]) - 2, len(maze) - 2, -1)

def expandHorizontally(maze):
    tmp = [0, 0, 0]
    lines = [0 for i in range(len(maze))]
    for i in range(len(maze)):
        sb = StringBuilder(maze[i].length * 2)
        for j in range(len(maze[i])):
            if j % 2 == 0:
                sb.append(maze[i][j])
            else:
                tmp[0] = tmp[1] = tmp[2] = maze[i][j]
                if tmp[1] == '*':
                    tmp[0] = tmp[2] = ' '
                sb.append(tmp)
        lines[i] = sb.toString()
    return lines

def main(args):
    f = FileInputStream(args[0]) if len(args) > 0 else System.in
    lines = readLines(f)
    maze = decimateHorizontally(lines)
    solveMaze(maze)
    solvedLines = expandHorizontally(maze)
    for i in range(len(solvedLines)):
        System.out.println(solvedLines[i])
```