class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def determinant(self):
        # code to calculate determinant

    def cofactors(self):
        # code to calculate cofactors

    def replace_column(self, column, constants):
        # code to replace column with constants


def cramer_rule(matrix, constants):
    # code to solve system of equations using Cramer's Rule


if __name__ == "__main__":
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    constants = [10, 11, 12]
    cramer_rule(matrix, constants)