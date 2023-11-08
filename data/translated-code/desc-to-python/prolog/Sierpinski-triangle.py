```python
def sierpinski_triangle(N):
    cells = [[' ' for _ in range(N)] for _ in range(N)]
    cells[N//2][0] = '*'

    for i in range(N-1):
        for j in range(N-i-1):
            if cells[i][j] == cells[i][j+2]:
                cells[i+1][j+1] = ' '
            else:
                cells[i+1][j+1] = '*'

    for row in cells:
        print(''.join(row))
```