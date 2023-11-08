```python
import Data.List
import Text.Printf

def spiral(height, width, start):
    def generate_spiral(n, m, start):
        if n == 0 or m == 0:
            return []
        elif n == 1:
            return [[start + i for i in range(m)]]
        elif m == 1:
            return [[start + i] for i in range(n)]
        else:
            top_row = [start + i for i in range(m)]
            right_col = [start + m + i for i in range(n-1)]
            bottom_row = [start + m + n - 1 + i for i in range(m-1)]
            left_col = [start + m + 2*n - 2 + i for i in range(n-2)]
            inner_spiral = generate_spiral(n-2, m-2, start + 2*n + 2*m - 2)
            return [top_row] + list(map(\r -> [last r] + r) inner_spiral) + [reverse left_col] + [reverse bottom_row] + [reverse right_col]

    spiral = generate_spiral(height, width, start)
    return transpose(spiral)

def main():
    height = 5
    width = 5
    start = 1
    spiral_pattern = spiral(height, width, start)
    for row in spiral_pattern:
        for num in row:
            printf("%3d" % num)
        print()

main()
```