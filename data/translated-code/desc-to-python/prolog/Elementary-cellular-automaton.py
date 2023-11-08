```python
# Define rules for the cellular automaton
def r(state, x):
    # Rules for determining next state based on current state and neighborhood
    pass

# Apply rules to current state to calculate next state
def apply_rules(current_state):
    # Code to apply the rules to the current state and calculate the next state
    pass

# Print the current state of the automaton
def writ(state):
    # Code to print the current state of the automaton
    pass

# Initiate automaton with initial state and run for 50 iterations
def play(initial_state):
    state = initial_state
    for i in range(50):
        writ(state)
        state = apply_rules(state)

# Example usage
initial_state = [0, 1, 0, 1, 0]
play(initial_state)
```