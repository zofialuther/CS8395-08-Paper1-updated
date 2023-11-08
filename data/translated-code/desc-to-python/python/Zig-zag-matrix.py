def zigzag(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matrix[i][j] = num
                num += 1
        else:
            for j in range(n-1, -1, -1):
                matrix[i][j] = num
                num += 1
    return matrix

def printzz(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

pattern = zigzag(6)
printzz(pattern)