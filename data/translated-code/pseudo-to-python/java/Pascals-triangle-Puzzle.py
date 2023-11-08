```python
class Matrix:
    def __init__(self, *args):
        self.matrix = list(args)
    
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
    
    def determinant(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        elif len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            total = 0
            for i in range(len(self.matrix)):
                total += ((-1) ** i) * self.matrix[0][i] * self.coFactor(0, i).determinant()
            return total
    
    def coFactor(self, row, col):
        new_matrix = [row[:col] + row[col+1:] for row in (self.matrix[:row]+self.matrix[row+1:])]
        return Matrix(*new_matrix)
    
    def replaceColumn(self, b, col):
        new_matrix = [self.matrix[i][:col] + [b[i]] + self.matrix[i][col+1:] for i in range(len(self.matrix))]
        return Matrix(*new_matrix)
    
    def get(self, row, col):
        return self.matrix[row][col]

def cramersRule(matrix, b):
    denominator = matrix.determinant()
    result = []
    for elem in b:
        modified_matrix = matrix.replaceColumn(b, b.index(elem))
        result.append(modified_matrix.determinant() / denominator)
    return result

def main():
    matrix = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    b = [10, 11, 12]
    solution = cramersRule(matrix, b)
    print("Solution =", cramersRule(matrix, b))
    print("X =", solution[0])
    print("Y =", solution[1])
    print("Z =", solution[2])

main()
```