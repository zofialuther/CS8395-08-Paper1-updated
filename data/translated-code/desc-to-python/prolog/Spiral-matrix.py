```python
def spiral(N):
    grid = [[-1 for _ in range(N)] for _ in range(N)]
    
    def spiralH(x, y, dx, dy, n):
        if n == N*N:
            return grid
        if 0 <= x < N and 0 <= y < N and grid[x][y] == -1:
            grid[x][y] = n
            return spiralH(x+dx, y+dy, dx, dy, n+1)
        else:
            return spiralH(x-dx, y-dy, -dy, dx, n)
    
    return spiralH(0, 0, 0, 1, 0)
```