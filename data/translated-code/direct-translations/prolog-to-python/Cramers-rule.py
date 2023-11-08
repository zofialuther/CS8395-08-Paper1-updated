```python
def removeElement(lst, j):
    if j == 0:
        return lst[1:]
    else:
        return [lst[0]] + removeElement(lst[1:], j - 1)

def removeColumn(matrix, j):
    if not matrix:
        return []
    else:
        return [removeElement(matrix[0], j)] + removeColumn(matrix[1:], j)

def removeRow(matrix, i):
    if i == 0:
        return matrix[1:]
    else:
        return [matrix[0]] + removeRow(matrix[1:], i - 1)

def cofactor(matrix, i, j):
    matrix_2 = removeRow(matrix, i)
    matrix_3 = removeColumn(matrix_2, j)
    y = det(matrix_3)
    return (-1) ** (i + j) * y

def det_summand(matrix, j, b):
    if not b:
        return 0
    else:
        b_head, *b_tail = b
        z = cofactor(matrix, 0, j)
        y = det_summand(matrix, j + 1, b_tail)
        return b_head * z + y

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        matrix_head = matrix[0]
        return det_summand(matrix, 0, matrix_head)

def replaceElement(lst, j, new):
    if j == 0:
        return [new] + lst[1:]
    else:
        return [lst[0]] + replaceElement(lst[1:], j - 1, new)

def replaceColumn(matrix, j, column):
    if not matrix:
        return []
    else:
        return [replaceElement(matrix[0], j, column[0])] + replaceColumn(matrix[1:], j, column[1:])

def cramerElements(a, b, j):
    if j == len(b):
        return []
    else:
        a_j = replaceColumn(a, j, b)
        det_a_j = det(a_j)
        det_a = det(a)
        x_j = det_a_j / det_a
        return [x_j] + cramerElements(a, b, j + 1)

def cramer(a, b):
    return cramerElements(a, b, 0)

def results():
    a = [
        [2, -1,  5,  1],
        [3,  2,  2, -6],
        [1,  3,  3, -1],
        [5, -2, -3,  3]
    ]
    b = [-3, -32, -47, 49]
    return cramer(a, b)

print(results())
```