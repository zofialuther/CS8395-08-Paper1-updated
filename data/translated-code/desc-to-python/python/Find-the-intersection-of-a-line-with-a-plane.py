```python
import numpy as np

def LinePlaneCollision(plane_normal, plane_point, ray_direction, ray_point):
    ndotu = plane_normal.dot(ray_direction)
    if abs(ndotu) < 1e-6:
        return None
    w = ray_point - plane_point
    si = -plane_normal.dot(w) / ndotu
    Psi = ray_point + si * ray_direction
    return Psi

plane_normal = np.array([1, 1, 1])
plane_point = np.array([0, 0, 0])
ray_direction = np.array([1, -1, 0])
ray_point = np.array([1, 1, 1])

result = LinePlaneCollision(plane_normal, plane_point, ray_direction, ray_point)
print(result)
```