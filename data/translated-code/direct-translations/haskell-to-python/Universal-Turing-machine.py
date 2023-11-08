def beaver(input_symbol, state, tape):
    if state == "a":
        if input_symbol == 0:
            return ("Action", 1, "MRight", "b")
        elif input_symbol == 1:
            return ("Action", 1, "MLeft", "c")
    elif state == "b":
        if input_symbol == 0:
            return ("Action", 1, "MLeft", "a")
        elif input_symbol == 1:
            return ("Action", 1, "MRight", "b")
    elif state == "c":
        if input_symbol == 0:
            return ("Action", 1, "MLeft", "b")
        elif input_symbol == 1:
            return ("Action", 1, "Stay", "halt")

def tape(index, left, right):
    return (index, left, right)

def runUTM(transition_function, initial_state, tape):
    current_state = initial_state
    current_index = tape[0]
    left_tape = tape[1]
    right_tape = tape[2]
    
    while current_state != "halt":
        current_symbol = right_tape[0] if current_index == 0 else left_tape[-1] if current_index == -1 else right_tape[current_index - 1]
        action, move, new_state, new_symbol = transition_function(current_symbol, current_state, tape)
        
        if action == "Action":
            if move == 1:
                if current_index == 0:
                    right_tape = [new_symbol] + right_tape
                elif current_index == -1:
                    left_tape = left_tape[:-1] + [new_symbol]
                else:
                    right_tape[current_index - 1] = new_symbol
                current_index += 1
            elif move == -1:
                if current_index == 0:
                    right_tape = right_tape[1:]
                elif current_index == -1:
                    left_tape = [new_symbol] + left_tape
                    current_index += 1
                else:
                    right_tape[current_index - 1] = new_symbol
                    current_index -= 1
            current_state = new_state
    
    return tape(current_index, left_tape, right_tape)

tape2 = tape(0, [], [])
machine2 = runUTM(beaver, "a", tape2)