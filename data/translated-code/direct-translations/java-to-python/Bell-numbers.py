```python
class BellTriangle:
    def __init__(self, n):
        length = n * (n + 1) // 2
        self.arr = [0] * length

        self.set(1, 0, 1)
        for i in range(2, n+1):
            self.set(i, 0, self.get(i - 1, i - 2))
            for j in range(1, i):
                value = self.get(i, j - 1) + self.get(i - 1, j - 1)
                self.set(i, j, value)

    def index(self, row, col):
        if row > 0 and col >= 0 and col < row:
            return row * (row - 1) // 2 + col
        else:
            raise ValueError()

    def get(self, row, col):
        i = self.index(row, col)
        return self.arr[i]

    def set(self, row, col, value):
        i = self.index(row, col)
        self.arr[i] = value

def main():
    rows = 15
    bt = BellTriangle(rows)

    print("First fifteen Bell numbers:")
    for i in range(rows):
        print("%2d: %d" % (i + 1, bt.get(i + 1, 0)))

    for i in range(1, 11):
        print(bt.get(i, 0), end='')
        for j in range(1, i):
            print(", %d" % bt.get(i, j), end='')
        print()

if __name__ == "__main__":
    main()
```