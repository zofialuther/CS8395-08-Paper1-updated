def identity(size):
    matrix = [[0]*size for i in range(size)]

    for i in range(size):
        matrix[i][i] = 1

    for rows in matrix:
        for elements in rows:
            print(elements, end=' ')
        print("")