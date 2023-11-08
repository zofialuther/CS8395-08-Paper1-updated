def push(ELEMENT, STACK):
    return [ELEMENT] + STACK

def pop(STACK):
    return STACK[0], STACK[1:]

def empty(STACK):
    return len(STACK) == 0