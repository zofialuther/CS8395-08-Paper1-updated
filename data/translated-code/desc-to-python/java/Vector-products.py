```python
class VectorProds:
    class Vector3D:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def dot_product(self, other):
            return self.x * other.x + self.y * other.y + self.z * other.z

        def cross_product(self, other):
            return Vector3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

        def scalar_triple_product(self, other1, other2):
            return self.dot_product(other1.cross_product(other2))

        def vector_triple_product(self, other1, other2):
            return self.cross_product(other1.cross_product(other2))

    def main(self):
        vector1 = Vector3D(1, 2, 3)
        vector2 = Vector3D(4, 5, 6)
        vector3 = Vector3D(7, 8, 9)

        dot_result = vector1.dot_product(vector2)
        cross_result = vector1.cross_product(vector2)
        scalar_triple_result = vector1.scalar_triple_product(vector2, vector3)
        vector_triple_result = vector1.vector_triple_product(vector2, vector3)

        print(dot_result, cross_result.x, cross_result.y, cross_result.z, scalar_triple_result, vector_triple_result.x, vector_triple_result.y, vector_triple_result.z)

# Instantiate the VectorProds class and call the main method
vp = VectorProds()
vp.main()
```