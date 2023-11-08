```python
def average(p1, p2):
    return ((p1[0]+p2[0])//2, (p1[1]+p2[1])//2)

def notBlocked(maze, pos):
    return maze[pos[0]][pos[1]] != '#'

def substitute(lst, pos, elem):
    lst[pos[0]] = lst[pos[0]][:pos[1]] + elem + lst[pos[0]][pos[1]+1:]
    return lst

def draw(maze, pos):
    maze[pos[0]] = maze[pos[0]][:pos[1]] + '*' + maze[pos[0]][pos[1]+1:]
    return maze

def tryMoves(maze, pos):
    # implementation of tryMoves function

def solve_(maze, pos):
    # implementation of solve_ function

def solve(maze):
    # implementation of solve function

def main(maze):
    # implementation of main function
```