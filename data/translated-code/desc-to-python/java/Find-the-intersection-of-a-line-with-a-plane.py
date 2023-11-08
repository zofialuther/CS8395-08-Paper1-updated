```python
class LinePlaneIntersection:
    class Vector3D:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    @staticmethod
    def intersectPoint(ray_origin, ray_direction, plane_point, plane_normal):
        # perform intersection calculation using vector operations
        # ...
        return intersection_point

# main method
if __name__ == "__main__":
    ray_origin = LinePlaneIntersection.Vector3D(1, 2, 3)
    ray_direction = LinePlaneIntersection.Vector3D(4, 5, 6)
    plane_point = LinePlaneIntersection.Vector3D(7, 8, 9)
    plane_normal = LinePlaneIntersection.Vector3D(10, 11, 12)

    intersection_point = LinePlaneIntersection.intersectPoint(ray_origin, ray_direction, plane_point, plane_normal)
    print(intersection_point.x, intersection_point.y, intersection_point.z)
```