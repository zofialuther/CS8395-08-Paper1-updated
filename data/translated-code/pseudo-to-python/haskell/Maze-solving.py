def average(a, b):
    return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2

def notBlocked(directions, edges):
    return all(d not in edges for d in directions)

def substitute(arr, i, val):
    arr[i] = val
    return arr

def draw(maze, pos):
    x, y = pos
    new_maze = maze[:]
    new_maze[y] = substitute(new_maze[y], x, 'x')
    return new_maze

def tryMoves(maze, pos, moves):
    new_pos = [(average(a, b)) for a, b in moves]
    return [p for p in new_pos if notBlocked([' ', 'x'], (pos, p))]

def solve_(maze, start, end):
    if start == end:
        return [end]
    moves = tryMoves(maze, start, [(0, 1), (0, -1), (1, 0), (-1, 0)])
    for move in moves:
        path = solve_(draw(maze, start), move, end)
        if path:
            return [start] + path
    return []

def solve(maze):
    start = (0, maze[0].index(' '))
    end = (len(maze) - 1, maze[-1].index(' '))
    return solve_(maze, start, end)

def main():
    main_ = lambda input_data: '\n'.join(solve(input_data)) if solve(input_data) else "can't solve"
    interact(main_)