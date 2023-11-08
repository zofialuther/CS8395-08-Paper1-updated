def multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(sum(map(lambda x, y: x * y, matrix1[i], [row[j] for row in matrix2])))
        result.append(row)
    return result

def main():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result_matrix = multiply(matrix1, matrix2)
    for row in result_matrix:
        print(row)

main()