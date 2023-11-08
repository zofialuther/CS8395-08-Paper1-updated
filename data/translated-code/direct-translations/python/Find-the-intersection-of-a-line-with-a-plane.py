```python
import numpy as np

def LinePlaneCollision(planeNormal, planePoint, rayDirection, rayPoint, epsilon=1e-6):
    ndotu = np.dot(planeNormal, rayDirection)
    if abs(ndotu) < epsilon:
        raise RuntimeError("no intersection or line is within plane")
    
    w = rayPoint - planePoint
    si = -np.dot(planeNormal, w) / ndotu
    Psi = w + si * rayDirection + planePoint
    return Psi

if __name__=="__main__":
    #Define plane
    planeNormal = np.array([0, 0, 1])
    planePoint = np.array([0, 0, 5]) #Any point on the plane

    #Define ray
    rayDirection = np.array([0, -1, -1])
    rayPoint = np.array([0, 0, 10]) #Any point along the ray

    Psi = LinePlaneCollision(planeNormal, planePoint, rayDirection, rayPoint)
    print("intersection at", Psi)
```