```python
# Point
def point_construct(X, Y):
    X1 = X if X else 0
    Y1 = Y if Y else 0
    return (X1, Y1)

# Circle
def circle_construct(X, Y, R):
    X1 = X if X else 0
    Y1 = Y if Y else 0
    R1 = R if R else 0
    return (X1, Y1, R1)

# Accessors for general X,Y
def shape_x_y_set(shape, X, Y):
    if len(shape) == 2:
        return (X, Y, shape[1])
    elif len(shape) == 3:
        return (X, Y, shape[2])

# Accessors for R
def circle_r_set(circle, R):
    return (circle[0], circle[1], R)

# Print
def print_shape(shape):
    if len(shape) == 2:
        print(f'Point ({shape[0]},{shape[1]})')
    elif len(shape) == 3:
        print(f'Circle ({shape[0]},{shape[1]},{shape[2]})')

# Default values for constructor (default to 0).
def default(N):
    if N is None:
        return 0
    elif isinstance(N, (int, float)):
        return N

# Tests
def test_point():
    P = point_construct(2, 3)
    test_poly(P)

def test_circle():
    C = circle_construct(3, 4, None)
    C1 = circle_r_set(C, 5)
    test_poly(C1)

def test_poly(T):
    X, Y, R = shape_x_y_set(T, T[0]*2, T[1]*2)
    T1 = (X, Y, R)
    print_shape(T1)
```