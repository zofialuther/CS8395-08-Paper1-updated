def spiral(n):
    arr = [[None for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1
    for i in range(1, n*n+1):
        arr[x][y] = i
        if (x+dx >= n or y+dy >= n or x+dx < 0 or y+dy < 0 or arr[x+dx][y+dy] is not None):
            dx, dy = dy, -dx
        x, y = x+dx, y+dy
    for row in arr:
        print(" ".join(["{:<3}".format(num) for num in row]))