```python
import random

class MazeGenerator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.maze = [[0 for _ in range(y)] for _ in range(x)]
        self.generateMaze(0, 0)

    def display(self):
        for i in range(self.y):
            # draw the north edge
            for j in range(self.x):
                print("+---" if (self.maze[j][i] & 1) == 0 else "+   ", end="")
            print("+")
            # draw the west edge
            for j in range(self.x):
                print("|   " if (self.maze[j][i] & 8) == 0 else "    ", end="")
            print("|")
        # draw the bottom line
        for j in range(self.x):
            print("+---", end="")
        print("+")

    def generateMaze(self, cx, cy):
        dirs = [(1, 0, -1), (2, 0, 1), (4, 1, 0), (8, -1, 0)]
        random.shuffle(dirs)
        for dir in dirs:
            bit, dx, dy = dir
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < self.x and 0 <= ny < self.y and self.maze[nx][ny] == 0:
                self.maze[cx][cy] |= bit
                self.maze[nx][ny] |= self.getOppositeBit(bit)
                self.generateMaze(nx, ny)

    def getOppositeBit(self, bit):
        if bit == 1:
            return 2
        elif bit == 2:
            return 1
        elif bit == 4:
            return 8
        elif bit == 8:
            return 4

if __name__ == "__main__":
    import sys
    x = int(sys.argv[1]) if len(sys.argv) >= 2 else 8
    y = int(sys.argv[2]) if len(sys.argv) == 3 else 8
    maze = MazeGenerator(x, y)
    maze.display()
```