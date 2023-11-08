```python
class Bell:
    class BellTriangle:
        def __init__(self, n):
            self.triangle = [[0 for i in range(n)] for j in range(n)]
            self.calculate_bell_numbers(n)

        def calculate_bell_numbers(self, n):
            self.triangle[0][0] = 1
            for i in range(1, n):
                self.triangle[i][0] = self.triangle[i-1][i-1]
                for j in range(1, i+1):
                    self.triangle[i][j] = self.triangle[i-1][j-1] + self.triangle[i][j-1]
        
        def get_bell_number(self, row, col):
            return self.triangle[row-1][col-1]

        def display_triangle(self, n):
            for i in range(n):
                for j in range(i+1):
                    print(self.triangle[i][j], end=" ")
                print()

    def main(self):
        bell_triangle = self.BellTriangle(15)
        for i in range(1, 16):
            print(f"Bell number {i}: {bell_triangle.get_bell_number(i, 1)}")
        print("\nTriangle of Bell numbers:")
        bell_triangle.display_triangle(10)

bell = Bell()
bell.main()
```