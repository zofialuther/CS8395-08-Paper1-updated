class CramersRule:
    def main(self):
        mat = Matrix([ [2.0, -1.0, 5.0, 1.0], [3.0, 2.0, 2.0, -6.0], [1.0, 3.0, 3.0, -1.0], [5.0, -2.0, -3.0, 3.0] ])
        b = [-3.0, -32.0, -47.0, 49.0]
        print("Solution = " + str(self.cramersRule(mat, b)))

    def cramersRule(self, matrix, b):
        denominator = matrix.determinant()
        result = []
        for i in b:
            result.append(matrix.replaceColumn(b, i).determinant() / denominator)
        return result

class Matrix:
    def __init__(self, *lists):
        self.matrix = [list for list in lists]

    def __init__(self, mat):
        self.matrix = mat

    def determinant(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        elif len(self.matrix) == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
        else:
            sum = 0
            sign = 1
            for i in range(len(self.matrix)):
                sum += sign * (self.matrix[0][i] * self.coFactor(0, i).determinant())
                sign = -sign
            return sum

    def coFactor(self, row, col):
        mat = []
        for i in range(len(self.matrix)):
            if i == row:
                continue
            list = []
            for j in range(len(self.matrix[i])):
                if j == col:
                    continue
                list.append(self.matrix[i][j])
            mat.append(list)
        return Matrix(mat)

    def replaceColumn(self, b, column):
        mat = []
        for row in range(len(self.matrix)):
            list = []
            for col in range(len(self.matrix[row])):
                value = self.matrix[row][col]
                if col == column:
                    value = b[row]
                list.append(value)
            mat.append(list)
        return Matrix(mat)

    def get(self, row, col):
        return self.matrix[row][col]