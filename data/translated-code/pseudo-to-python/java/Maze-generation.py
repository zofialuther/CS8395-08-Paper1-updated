class MazeGenerator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.maze = [[0 for j in range(y)] for i in range(x)]
        self.generateMaze(0, 0)
  
    def display(self):
        for i in range(self.y):
            for j in range(self.x):
                if (self.maze[j][i] & 1) == 0:
                    print("+---", end="")
                else:
                    print("+   ", end="")
            print("+")
            for j in range(self.x):
                if (self.maze[j][i] & 8) == 0:
                    print("|   ", end="")
                else:
                    print("    ", end="")
            print("|")
        for j in range(self.x):
            print("+---", end="")
        print("+")
  
    def generateMaze(self, cx, cy):
        from random import shuffle
        dirs = list(DIR)
        shuffle(dirs)
        for dir in dirs:
            nx = cx + dir.dx
            ny = cy + dir.dy
            if (self.between(nx, self.x) and self.between(ny, self.y) and self.maze[nx][ny] == 0):
                self.maze[cx][cy] |= dir.bit
                self.maze[nx][ny] |= dir.opposite.bit
                self.generateMaze(nx, ny)
  
    def between(self, v, upper):
        return (v >= 0) and (v < upper)
  
from enum import Enum

class DIR(Enum):
    N = (1, 0, -1)
    S = (2, 0, 1)
    E = (4, 1, 0)
    W = (8, -1, 0)
    opposite = None
  
    N.opposite = DIR.S
    S.opposite = DIR.N
    E.opposite = DIR.W
    W.opposite = DIR.E
  
    def __init__(self, bit, dx, dy):
        self.bit = bit
        self.dx = dx
        self.dy = dy
  
if __name__ == "__main__":
    import sys
    x = int(sys.argv[1]) if len(sys.argv) >= 2 else 8
    y = int(sys.argv[2]) if len(sys.argv) == 3 else 8
    maze = MazeGenerator(x, y)
    maze.display()