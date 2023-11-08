def grid(l):
    width = len(l[0])
    height = len(l)
    a = [[1]*width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            a[i][j] = l[i][j]
    return (width, height, a)

def printGrid(width, grid):
    for row in grid:
        print(' '.join(row))

def split(n, arr):
    result = []
    for i in range(0, len(arr), n):
        result.append(arr[i:i+n])
    return result

blinker = grid([
    ".#.",
    ".#.",
    ".#."
])

glider = grid([
    "............",
    "............",
    "............",
    ".......###..",
    ".......#....",
    "........#...",
    "............"
])

def printLife(n, (w, h, g)):
    for _ in range(n):
        print("------------------------------")
        printGrid(w, g)

main = printLife(10, glider)