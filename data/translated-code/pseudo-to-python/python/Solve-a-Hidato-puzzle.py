board = []
given = []
start = None

def setup(s):
    global board
    lines = s.splitlines()
    ncols = len(lines[0].split())
    nrows = len(lines)
    board = [[-1 for _ in range(ncols + 2)] for _ in range(nrows + 2)]

    for r in range(nrows):
        for c in range(ncols):
            cell = lines[r].split()[c]
            if cell == "__":
                board[r + 1][c + 1] = 0
                continue
            elif cell == ".":
                continue
            else:
                val = int(cell)
                board[r + 1][c + 1] = val
                given.append(val)
                if val == 1:
                    start = (r + 1, c + 1)
    given.sort()

def solve(r, c, n, next=0):
    global given
    if n > given[-1]:
        return True
    if board[r][c] and board[r][c] != n:
        return False
    if board[r][c] == 0 and given[next] == n:
        return False

    back = 0
    if board[r][c] == n:
        next = next + 1
        back = n

    board[r][c] = n
    for i in range(-1, 2):
        for j in range(-1, 2):
            if solve(r + i, c + j, n + 1, next):
                return True
    board[r][c] = back
    return False

def print_board():
    d = {-1: "  ", 0: "__"}
    bmax = max(max(row) for row in board)
    form = "%" + str(len(str(bmax)) + 1) + "s"
    for r in board[1:-1]:
        print("".join(form % d[elem] for elem in r[1:-1]))

hi = """\
__ 33 35 __ __  .  .  .
__ __ 24 22 __  .  .  .
__ __ __ 21 __ __  .  .
__ 26 __ 13 40 11  .  .
27 __ __ __  9 __  1  .
 .  . __ __ 18 __ __  .
 .  .  .  . __  7 __ __
 .  .  .  .  .  .  5 __"""

setup(hi)
print_board()
solve(start[0], start[1], 1)
print()
print_board()