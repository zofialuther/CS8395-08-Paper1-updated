def step(State):
    if isBlack(State):
        setWhite(State)
        turnRight(State)
    else:
        setBlack(State)
        turnLeft(State)
    move(State)

def isBlack(State):
    return State.p in State.m

def setBlack(State):
    State.m.append(State.p)

def setWhite(State):
    State.m.remove(State.p)

def turnRight(State):
    State.d = (State.d[1], -State.d[0])

def turnLeft(State):
    State.d = (-State.d[1], State.d[0])

def move(State):
    State.p = (State.p[0] + State.d[0], State.p[1] + State.d[1])