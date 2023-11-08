from math import sin, radians

# function to generate list of triangles with different angle measurements
def generate_triangles(max_side):
    triangles = []
    for angle in range(1, 91):
        side = max_side * sin(radians(angle))
        triangles.append((angle, side))
    return triangles

# lambda function to generate uneven triangles at a 60-degree angle
uneven_triangles = lambda max_side: [(60, max_side * sin(radians(60)))]

# dictionary manipulation to achieve the purpose
triangles_dict = {
    "max_13_triangles": generate_triangles(13),
    "max_10000_triangles": uneven_triangles(10000)
}