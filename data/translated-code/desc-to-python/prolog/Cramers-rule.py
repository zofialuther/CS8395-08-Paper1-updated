def remove_element(lst, element):
    lst.remove(element)
    return lst

def remove_column(matrix, col_index):
    for row in matrix:
        del row[col_index]
    return matrix

def remove_row(matrix, row_index):
    del matrix[row_index]
    return matrix

def calculate_cofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def find_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c) * matrix[0][c] * find_determinant(calculate_cofactor(matrix, 0, c))
    return determinant

def replace_element(lst, index, new_element):
    lst[index] = new_element
    return lst

def replace_column(matrix, col_index, new_col):
    for i in range(len(matrix)):
        matrix[i][col_index] = new_col[i]
    return matrix

def cramer_rule_elements(matrix, vector):
    det_A = find_determinant(matrix)
    elements = []
    for i in range(len(matrix)):
        new_matrix = replace_column(matrix, i, vector)
        elements.append(find_determinant(new_matrix) / det_A)
    return elements

def solve_linear_equations(matrix, vector):
    return cramer_rule_elements(matrix, vector)

def results():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [1, 2, 3]
    X = solve_linear_equations(A, B)
    print(X)