def replace(list, index, element, result):
    if index == 0:
        result = [element] + list[1:]
    else:
        result = [list[0]] + replace(list[1:], index-1, element, result)

def replace_in(grid, coordinates, element, result):
    if coordinates[0] == 0:
        new_row = replace(grid[coordinates[0]], coordinates[1], element, [])
        result = [new_row] + grid[1:]
    else:
        new_row = grid[coordinates[0]][:]
        new_row = replace(new_row, coordinates[1], element, [])
        result = [new_row] + replace_in(grid[1:], (coordinates[0]-1, coordinates[1]), element, [])

def get_in(grid, coordinates, element):
    element = grid[coordinates[0]][coordinates[1]]

def create(size, matrix):
    Ns = []
    for i in range(1, size+1):
        Ns.append(i)
    Ls = [None] * size
    X = [Ls[:] for _ in range(size)]
    matrix = X

def ops(direction, coordinates, result1, result2, new_direction1, new_direction2):
    if direction == "right":
        result1[0] = coordinates[0]
        result1[1] = coordinates[1] + 1
        new_direction1 = "right"
        result2[0] = coordinates[0] + 1
        result2[1] = coordinates[1]
        new_direction2 = "down"
    elif direction == "left":
        result1[0] = coordinates[0]
        result1[1] = coordinates[1] - 1
        new_direction1 = "left"
        result2[0] = coordinates[0] - 1
        result2[1] = coordinates[1]
        new_direction2 = "up"
    elif direction == "up":
        result1[0] = coordinates[0] - 1
        result1[1] = coordinates[1]
        new_direction1 = "up"
        result2[0] = coordinates[0]
        result2[1] = coordinates[1] + 1
        new_direction2 = "right"
    elif direction == "down":
        result1[0] = coordinates[0] + 1
        result1[1] = coordinates[1]
        new_direction1 = "down"
        result2[0] = coordinates[0]
        result2[1] = coordinates[1] - 1
        new_direction2 = "left"

def next(direction, matrix, coordinates, new_coordinates, new_direction):
    C1 = [0, 0]
    C2 = [0, 0]
    D1 = ""
    D2 = ""
    ops(direction, coordinates, C1, C2, D1, D2)
    if get_in(matrix, C1, None) == None:
        new_coordinates = C1
        new_direction = D1
    else:
        new_coordinates = C2
        new_direction = D2

def spiralH(direction, matrix, coordinates, elements, result):
    new_matrix = []
    replace_in(matrix, coordinates, elements[0], new_matrix)
    if elements == []:
        result = new_matrix
    else:
        new_coordinates = [0, 0]
        new_direction = ""
        next(direction, matrix, coordinates, new_coordinates, new_direction)
        spiralH(new_direction, new_matrix, new_coordinates, elements[1:], result)

def spiral(size, matrix):
    Sq = size*size - 1
    Ns = [i for i in range(Sq+1)]
    EMx = []
    create(size, EMx)
    spiralH("right", EMx, [0, 0], Ns, matrix)