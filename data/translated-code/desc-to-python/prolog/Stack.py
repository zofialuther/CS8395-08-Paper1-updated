def push(element, stack):
    stack.append(element)
    return True

def pop(stack):
    if len(stack) > 0:
        stack.pop()
        return True
    else:
        return False

def empty(stack):
    return len(stack) == 0