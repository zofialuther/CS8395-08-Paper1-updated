```python
def vector_plus(U, V):
    X3 = U[0] + V[0]
    Y3 = U[1] + V[1]
    Z3 = U[2] + V[2]
    return (X3, Y3, Z3)

def vector_minus(U, V):
    X3 = U[0] - V[0]
    Y3 = U[1] - V[1]
    Z3 = U[2] - V[2]
    return (X3, Y3, Z3)

def vector_times(U, S):
    X2 = U[0] * S
    Y2 = U[1] * S
    Z2 = U[2] * S
    return (X2, Y2, Z2)

def vector_dot(U, V):
    S = U[0] * V[0] + U[1] * V[1] + U[2] * V[2]
    return S

def intersect_point(RayVector, RayPoint, PlaneNormal, PlanePoint):
    Diff = vector_minus(RayPoint, PlanePoint)
    Prod1 = vector_dot(Diff, PlaneNormal)
    Prod2 = vector_dot(RayVector, PlaneNormal)
    Prod3 = Prod1 / Prod2
    Times = vector_times(RayVector, Prod3)
    IntersectPoint = vector_minus(RayPoint, Times)
    return IntersectPoint

RayVector = (0.0, -1.0, -1.0)
RayPoint = (0.0, 0.0, 10.0)
PlaneNormal = (0.0, 0.0, 1.0)
PlanePoint = (0.0, 0.0, 5.0)
IntersectPoint = intersect_point(RayVector, RayPoint, PlaneNormal, PlanePoint)
print(f"The ray intersects the plane at {IntersectPoint}")
```