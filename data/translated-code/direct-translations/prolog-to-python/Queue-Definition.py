def empty(U, V):
    return unify_with_occurs_check(U, V)

def push(Queue, Value, NewQueue):
    X = Queue[1]
    Y = Queue[2]
    Z = NewQueue[2]
    NewQueue = (Queue[0], [Value] + X, Z)

def pop(Queue, X, NewQueue):
    X = Queue[0]
    V = Queue[1]
    U = Queue[2]
    if not empty([X, V]-U):
        NewQueue = (V, U)