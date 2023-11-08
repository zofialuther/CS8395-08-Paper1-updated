import numpy as np

def createMatrix(rows, cols, data):
    return np.array(data)

def printMatrix(matrix):
    print(matrix)

a = createMatrix(3, 2, [[1, 2], [3, 4], [5, 6]])

printMatrix(a)
printMatrix(np.transpose(a))