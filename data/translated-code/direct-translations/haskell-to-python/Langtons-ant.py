def step(state):
    def isBlack(state):
        return state[0] in state[2]
    
    def setBlack(state):
        return (state[0], state[1], state[2].add(state[0]))
    
    def setWhite(state):
        return (state[0], state[1], state[2].remove(state[0]))
    
    def turnRight(state):
        return (state[0], (state[1][1], -state[1][0]), state[2])
    
    def turnLeft(state):
        return (state[0], (-state[1][1], state[1][0]), state[2])
    
    def move(state):
        return ((state[0][0]+state[1][0], state[0][1]+state[1][1]), state[1], state[2])
    
    if isBlack(state):
        return (setWhite(state) >>> turnRight(state), move(state))
    else:
        return (setBlack(state) >>> turnLeft(state), move(state))