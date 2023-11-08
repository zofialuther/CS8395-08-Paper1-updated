```python
class GameOfLife:
    def __init__(self):
        pass

    def setGame(self):
        config = [['_' for j in range(60)] for i in range(20)]
        self.startGame(config, 20, 60)

    def startGame(self, mat, l, b):
        ch = ''
        while ch != "y":
            per = self.setConfig(mat)
            self.display2D(mat)
            print("Percentage of grid filled: ", per)
            ch = input("Begin? y/n")
        ch = ''
        while ch != "x":
            mat = self.transform(mat, l, b)
            self.display2D(mat)
            print("Ctrl+Z to stop")
            try:
                import time
                time.sleep(0.1)
            except Exception as e:
                print("Something went horribly wrong.")
            ch = input()
        print("Game Over")

    def transform(self, mat, l, b):
        newmat = [['_' for j in range(b)] for i in range(l)]
        for i in range(l):
            for j in range(b):
                newmat[i][j] = self.flip(mat, i, j)
        return newmat

    def flip(self, mat, i, j):
        count = self.around(mat, i, j)
        if mat[i][j] == '*':
            if count < 2 or count > 3:
                return '_'
            else:
                return '*'
        else:
            if count == 3:
                return '*'
            else:
                return '_'

    def around(self, mat, i, j):
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x, y) != (i, j):
                    count += self.eval(mat, x, y)
        return count

    def eval(self, mat, i, j):
        if i < 0 or j < 0 or i == len(mat) or j == len(mat[0]):
            return 0
        if mat[i][j] == '*':
            return 1
        else:
            return 0

    def setCustomConfig(self, arr, infile):
        try:
            with open(infile, 'r') as file:
                for i in range(len(arr)):
                    line = file.readline()
                    for j in range(len(arr[i])):
                        arr[i][j] = line[j]
        except Exception as e:
            print(e.getMessage())
        return 0

    def setConfig(self, arr):
        per = 0.10
        for i in range(len(arr)):
            self.setConfig1D(arr[i], per)
        return per

    def setConfig1D(self, arr, per):
        import random
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
```