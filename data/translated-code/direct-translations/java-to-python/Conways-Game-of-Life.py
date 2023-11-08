```python
import random
import time

class GameOfLife:
    # Set grid size
    l = 20
    b = 60

    def __init__(self):
        self.setGame()

    def setGame(self):
        config = [['_' for _ in range(self.b)] for _ in range(self.l)]
        self.startGame(config, self.l, self.b)

    def startGame(self, mat, l, b):
        ch = ""
        per = 0
        while ch != "y":
            per = self.setConfig(mat)
            self.display2D(mat)
            print(f"{per*100}% of grid filled.")
            ch = input("Begin? y/n")
        while ch != "x":
            mat = self.transform(mat, l, b)
            self.display2D(mat)
            print("Ctrl+Z to stop.")
            time.sleep(0.1)
            # ch = input()
        print("Game Over")

    def transform(self, mat, l, b):
        newmat = [['_' for _ in range(b)] for _ in range(l)]
        for i in range(l):
            for j in range(b):
                newmat[i][j] = self.flip(mat, i, j)
        return newmat

    def flip(self, mat, i, j):
        count = self.around(mat, i, j)
        if mat[i][j] == '*':
            if count < 2 or count > 3:
                return '_'
            return '*'
        else:
            if count == 3:
                return '*'
            return '_'

    def around(self, mat, i, j):
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j:
                    continue
                count += self.eval(mat, x, y)
        return count

    def eval(self, mat, i, j):
        if i < 0 or j < 0 or i == self.l or j == self.b:
            return 0
        if mat[i][j] == '*':
            return 1
        return 0

    def setCustomConfig(self, arr, infile):
        try:
            with open(infile, 'r') as file:
                for i in range(len(arr)):
                    line = file.readline()
                    for j in range(len(arr[0])):
                        arr[i][j] = line[j]
        except Exception as e:
            print(e)
        return 0

    def setConfig(self, arr):
        # Enter percentage of grid to be filled.
        per = 0.10
        for i in range(len(arr)):
            self.setConfig1D(arr[i], per)
        return per

    def setConfig1D(self, arr, per):
        for i in range(len(arr)):
            if random.random() < per:
                arr[i] = '*'
            else:
                arr[i] = '_'

    def display2D(self, arr):
        for i in range(len(arr)):
            self.display1D(arr[i])
        print()

    def display1D(self, arr):
        for i in range(len(arr)):
            print(arr[i], end='')
        print()


if __name__ == "__main__":
    GameOfLife()
```