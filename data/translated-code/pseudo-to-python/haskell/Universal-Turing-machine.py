def runUTM(program, halt_state, initial_state, tape):
    current_state = initial_state
    while current_state != halt_state:
        symbol = tape[0]
        action = beaver(symbol, current_state)
        tape[0] = action[2]
        if action[1] == "MRight":
            tape.insert(0, tape.pop())
        elif action[1] == "MLeft":
            tape.append(tape.pop(0))
        current_state = int(action[0])
    return tape

def beaver(symbol, state):
    if symbol == "a" and state == 0:
        return [1, "MRight", "b"]
    elif symbol == "a" and state == 1:
        return [1, "MLeft", "c"]
    elif symbol == "b" and state == 0:
        return [1, "MLeft", "a"]
    elif symbol == "b" and state == 1:
        return [1, "MRight", "b"]
    elif symbol == "c" and state == 0:
        return [1, "MLeft", "b"]
    elif symbol == "c" and state == 1:
        return [1, "Stay", "halt"]

tape2 = ["a"] + ["0"] * 10
machine2 = runUTM(beaver, "halt", 0, tape2)