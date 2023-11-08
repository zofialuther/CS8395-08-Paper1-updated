```python
class Matrix:

    def __init__(self, *lists):
        self.matrix = [list(l) for l in lists]

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
            list = []
            for j in range(len(self.matrix)):
                if j == col:
                    continue
                list.append(self.get(i, j))
            mat.append(list)
        return Matrix(*mat)

    def replaceColumn(self, b, column):
        mat = []
        for row in range(len(self.matrix)):
            list = []
            for col in range(len(self.matrix)):
                value = self.get(row, col)
                if col == column:
                    value = b[row]
                list.append(value)
            mat.append(list)
        return Matrix(*mat)

    def get(self, row, col):
        return self.matrix[row][col]


def cramersRule(matrix, b):
    denominator = matrix.determinant()
    result = []
    for i in range(len(b)):
        result.append(matrix.replaceColumn(b, i).determinant() / denominator)
    return result


if __name__ == "__main__":
    mat = Matrix([1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0])
    b = [11, 11, 0, 4, 4, 40, 0, 0, 40, 0, 151]
    solution = cramersRule(mat, b)
    print("Solution =", cramersRule(mat, b))
    print("X = {:.2f}".format(solution[8]))
    print("Y = {:.2f}".format(solution[9]))
    print("Z = {:.2f}".format(solution[10]))
```