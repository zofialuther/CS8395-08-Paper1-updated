```python
class NQueens:
    b = [0] * 8
    s = 0

    @staticmethod
    def unsafe(y):
        x = NQueens.b[y]
        for i in range(1, y+1):
            t = NQueens.b[y - i]
            if t == x or t == x - i or t == x + i:
                return True
        return False

    @staticmethod
    def putboard():
        print("\n\nSolution " + str(NQueens.s))
        for y in range(8):
            for x in range(8):
                print("|Q" if NQueens.b[y] == x else "|_", end="")
            print("|")

    @staticmethod
    def main():
        y = 0
        NQueens.b[0] = -1
        while y >= 0:
            while NQueens.b[y] < 8 and NQueens.unsafe(y):
                NQueens.b[y] += 1
            if NQueens.b[y] < 8:
                if y < 7:
                    y += 1
                    NQueens.b[y] = -1
                else:
                    NQueens.putboard()
            else:
                y -= 1


# Start of the program
NQueens.main()
```