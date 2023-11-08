class StateTapeSymbolPair:
    def __init__(self, state, tape_symbol):
        self.state = state
        self.tape_symbol = tape_symbol

class Transition:
    def __init__(self, current_state, current_symbol, new_state, new_symbol, direction):
        self.current_state = current_state
        self.current_symbol = current_symbol
        self.new_state = new_state
        self.new_symbol = new_symbol
        self.direction = direction

class UniversalTuringMachine:
    def __init__(self, transitions, terminal_states, initial_state, blank_symbol):
        self.transitions = transitions
        self.terminal_states = terminal_states
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol

    def initialize_tape(self, input_string):
        # implementation

    def run_machine(self):
        # implementation

# main method
if __name__ == "__main__":
    # instantiate UTM with transitions, terminal states, initial state, and blank symbol
    # perform simple tasks like incrementing numbers
    # perform more complex operations such as the Busy Beaver problem and sorting