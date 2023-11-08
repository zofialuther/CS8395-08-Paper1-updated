def empty(U, V):
    return unify_with_occurs_check(U, V)

def push(Queue, Value, NewQueue):
    X = Queue[1]
    Y = Queue[2]
    X.append(Value)
    NewQueue = [X, Y]

def pop(Queue, X, NewQueue):
    X = Queue[1][0]
    V = Queue[1][1]
    U = Queue[2]
    NewQueue = [V, U]

def not_empty(Queue):
    X = Queue[1]
    V = Queue[1][0]
    U = Queue[2]
    
    if empty([X, V]-U):
        return False
    else:
        return True

def append_dl(XY, YZ, XZ):
    X = XY[0]
    Y = XY[1]
    Z = YZ[1]
    XZ = [X, Z]