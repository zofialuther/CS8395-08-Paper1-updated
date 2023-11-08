def identity(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print('\n')

identity(3)