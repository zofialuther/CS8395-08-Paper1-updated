```python
def transpose(matrix):
    if not matrix:
        return matrix
    return [list(row) for row in zip(*matrix)]

# Transposing tuple of tuples
matrix1 = ((1, 2, 3), (4, 5, 6))
transposed_matrix1 = transpose(matrix1)
print("Original matrix:", matrix1, "Type:", type(matrix1))
print("Transposed matrix:", transposed_matrix1, "Type:", type(transposed_matrix1))

# Transposing tuple of lists
matrix2 = ([1, 2, 3], [4, 5, 6])
transposed_matrix2 = transpose(matrix2)
print("Original matrix:", matrix2, "Type:", type(matrix2))
print("Transposed matrix:", transposed_matrix2, "Type:", type(transposed_matrix2))

# Transposing list of lists
matrix3 = [[1, 2, 3], [4, 5, 6]]
transposed_matrix3 = transpose(matrix3)
print("Original matrix:", matrix3, "Type:", type(matrix3))
print("Transposed matrix:", transposed_matrix3, "Type:", type(transposed_matrix3))

# Transposing list of tuples
matrix4 = [(1, 2, 3), (4, 5, 6)]
transposed_matrix4 = transpose(matrix4)
print("Original matrix:", matrix4, "Type:", type(matrix4))
print("Transposed matrix:", transposed_matrix4, "Type:", type(transposed_matrix4))
```