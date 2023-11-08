def push(ELEMENT, STACK):
    STACK.insert(0, ELEMENT)

def pop(STACK):
    TOP = STACK[0]
    STACK = STACK[1:]
    return TOP, STACK

def empty(STACK):
    if not STACK:
        return True
    else:
        return False