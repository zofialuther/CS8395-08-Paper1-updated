```python
def point_construct(X, Y, point=(X1,Y1)):
    if X == None:
        X1 = 0
    else:
        X1 = X
    if Y == None:
        Y1 = 0
    else:
        Y1 = Y

def circle_construct(X, Y, R, circle=(X1,Y1,R1)):
    if X == None:
        X1 = 0
    else:
        X1 = X
    if Y == None:
        Y1 = 0
    else:
        Y1 = Y
    if R == None:
        R1 = 0
    else:
        R1 = R

def shape_x_y_set(point=(X,Y), X, Y):
    point = (X,Y)

def shape_x_y_set(circle=(X,Y,R), X, Y):
    circle = (X,Y,R)

def cicle_r_set(circle=(X,Y,_), R):
    circle = (X,Y,R)

def print_shape(point=(X,Y)):
    print("Point (~p,~p)" % (X, Y))

def print_shape(circle=(X,Y,R)):
    print("Circle (~p,~p,~p)" % (X, Y, R))

def default(N, 0):
    if N == None:
        N = 0
    elif type(N) == int or type(N) == float:
        N = N

def default(N, N):
    if N == None:
        N = N

def test_point():
    point_construct(2,3,P)
    test_poly(P)

def test_circle():
    circle_construct(3,4,_,C)
    cicle_r_set(C, 5, C1)
    test_poly(C1)

def test_poly(T):
    shape_x_y_set(_, X, Y, T)
    X1 = X * 2
    Y1 = Y * 2
    shape_x_y_set(T, X1, Y1, T1)
    print_shape(T1)
```