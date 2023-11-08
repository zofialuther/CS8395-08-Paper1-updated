def zig_zag(N):
    matrix = [[0 for i in range(N)] for j in range(N)]
    fill(matrix, N, 0, 0, 1)
    print_matrix(matrix)

def fill(matrix, N, row, col, val):
    if row < 0 or row >= N or col < 0 or col >= N:
        return
    matrix[row][col] = val
    next_val = compute_next(val, N, row, col)
    fill(matrix, N, row+1, col-1, next_val)

def compute_next(val, N, row, col):
    if (row + col) % 2 == 0:
        return val + N
    else:
        return val + 1

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(val) for val in row))