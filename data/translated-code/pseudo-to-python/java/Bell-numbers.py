class BellTriangle:
    def __init__(self, n):
        self.arr = [0] * (n * (n + 1) // 2)
        self.arr[0] = 1
    
    def index(self, row, col):
        return row * (row - 1) // 2 + col
    
    def get(self, row, col):
        return self.arr[self.index(row, col)]
    
    def set(self, row, col, value):
        self.arr[self.index(row, col)] = value

rows = 15
bt = BellTriangle(rows)
print("First fifteen Bell numbers:")
for i in range(1, rows + 1):
    print(bt.get(i, 0))
print("Bell triangle values for the first 10 rows:")
for i in range(1, 11):
    for j in range(i):
        print(bt.get(i, j), end=" ")
    print()