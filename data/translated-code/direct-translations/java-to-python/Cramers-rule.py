```python
class Matrix:
    def __init__(self, *lists):
        self.matrix = [list(lst) for lst in lists]

    def __str__(self):
        return str(self.matrix)

    def determinant(self):
        if len(self.matrix) == 1:
            return self.get(0, 0)
        if len(self.matrix) == 2:
            return self.get(0, 0) * self.get(1, 1) - self.get(0, 1) * self.get(1, 0)
        sum = 0
        sign = 1
        for i in range(len(self.matrix)):
            sum += sign * self.get(0, i) * self.coFactor(0, i).determinant()
            sign *= -1
        return sum

    def coFactor(self, row, col):
        mat = []
        for i in range(len(self.matrix)):
            if i == row:
                continue
            lst = []
            for j in range(len(self.matrix)):
                if j == col:
                    continue
                lst.append(self.get(i, j))
            mat.append(lst)
        return Matrix(mat)

    def replaceColumn(self, b, column):
        mat = []
        for row in range(len(self.matrix)):
            lst = []
            for col in range(len(self.matrix)):
                value = self.get(row, col)
                if col == column:
                    value = b[row]
                lst.append(value)
            mat.append(lst)
        return Matrix(mat)

    def get(self, row, col):
        return self.matrix[row][col]


def cramersRule(matrix, b):
    denominator = matrix.determinant()
    result = []
    for i in range(len(b)):
        result.append(matrix.replaceColumn(b, i).determinant() / denominator)
    return result


mat = Matrix([2, -1, 5, 1], [3, 2, 2, -6], [1, 3, 3, -1], [5, -2, -3, 3])
b = [-3, -32, -47, 49]
print("Solution = ", cramersRule(mat, b))
```