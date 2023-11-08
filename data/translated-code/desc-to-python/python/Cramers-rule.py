def det(m, n):
    if n == 1:
        return m[0][0]
    else:
        determinant = 0
        for i in range(n):
            sign = (-1) ** i
            sub_matrix = [[m[x][y] for y in range(n) if y != i] for x in range(1, n)]
            determinant += sign * m[0][i] * det(sub_matrix, n - 1)
        return determinant

h = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
w = 3
determinant = det(h, w)
if determinant != 0:
    inverse_matrix = [[(-1) ** (i + j) * det([row[:j] + row[j + 1:] for row in h[:i] + h[i + 1:]], w - 1) for j in range(w)] for i in range(w)]
    print(inverse_matrix)