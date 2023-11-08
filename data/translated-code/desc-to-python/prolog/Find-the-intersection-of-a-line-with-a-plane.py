```python
# Python code for vector operations and intersection calculation between ray and plane in 3D space

# Define vector addition
def vector_addition(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]

# Define vector subtraction
def vector_subtraction(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

# Define scalar multiplication
def scalar_multiplication(scalar, v):
    return [scalar * v[0], scalar * v[1], scalar * v[2]]

# Define dot product
def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

# Define intersection calculation between ray and plane
def ray_plane_intersection(ray_vector, ray_point, plane_normal, plane_point):
    d = dot_product(plane_normal, plane_point)
    t = (d - dot_product(plane_normal, ray_point)) / dot_product(plane_normal, ray_vector)
    intersection_point = vector_addition(ray_point, scalar_multiplication(t, ray_vector))
    return intersection_point

# Initialize values for ray vector, ray point, plane normal, and plane point
ray_vector = [1, 2, 3]
ray_point = [4, 5, 6]
plane_normal = [7, 8, 9]
plane_point = [10, 11, 12]

# Calculate intersection point of ray with plane
intersection_point = ray_plane_intersection(ray_vector, ray_point, plane_normal, plane_point)

# Format and print coordinates of intersection point
print(f"Intersection point coordinates: {intersection_point}")
```