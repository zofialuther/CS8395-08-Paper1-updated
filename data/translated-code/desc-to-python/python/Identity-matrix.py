def identity(size):
    matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    for row in matrix:
        print(' '.join(map(str, row)))
        
# Example usage
identity(3)