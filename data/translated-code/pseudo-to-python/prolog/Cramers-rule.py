```python
def removeElement(lst, j, result):
    if j == 0:
        result = lst[1:]
    else:
        result = [lst[0]] + removeElement(lst[1:], j-1, result)
    return result

def removeColumn(matrix, j, result):
    if not matrix:
        return []
    else:
        result.append(removeElement(matrix[0], j, []))
        return removeColumn(matrix[1:], j, result)

def removeRow(matrix, i, result):
    if i == 0:
        result = matrix[1:]
    else:
        result = [matrix[0]] + removeRow(matrix[1:], i-1, result)
    return result

def cofactor(matrix, i, j, result):
    matrix_2 = removeRow(matrix, i, [])
    matrix_3 = removeColumn(matrix_2, j, [])
    Y = det(matrix_3)
    result = ((-1) ** (i + j)) * Y
    return result

def det_summand(matrix, j, b, result):
    if not b:
        return 0
    else:
        b_head = b[0]
        Z = cofactor(matrix, 0, j, [])
        Y = det_summand(matrix, j + 1, b[1:], [])
        result = b_head * Z + Y
        return result

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        matrix_head = matrix[0]
        return det_summand(matrix, 0, matrix_head)

def replaceElement(lst, j, new, result):
    if j == 0:
        result = [new] + lst[1:]
    else:
        result = [lst[0]] + replaceElement(lst[1:], j-1, new, result)
    return result

def replaceColumn(matrix, j, column, result):
    if not matrix:
        return []
    else:
        result.append(replaceElement(matrix[0], j, column[0], []))
        return replaceColumn(matrix[1:], j, column[1:], result)

def cramerElements(A, B, j, result):
    if len(B) == j:
        return len(B)
    else:
        A_J = replaceColumn(A, j, B, [])
        Det_A_J = det(A_J)
        Det_A = det(A)
        result.append(Det_A_J / Det_A)
        return cramerElements(A, B, j + 1, result)

def cramer(A, B, X):
    X = cramerElements(A, B, 0, [])

def results(X):
    A = [
            [2, -1,  5,  1],
            [3,  2,  2, -6],
            [1,  3,  3, -1],
            [5, -2, -3,  3]
        ]
    B = [-3, -32, -47, 49]
    cramer(A, B, X)
```