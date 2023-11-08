```python
# Define rules for the beaver machine
rules = {
    ('A', '0'): ('B', '1', 'R'),
    ('A', '1'): ('C', '0', 'L'),
    ('B', '0'): ('A', '1', 'L'),
    ('B', '1'): ('B', '1', 'R'),
    ('C', '0'): ('B', '1', 'L'),
    ('C', '1'): ('H', '0', 'N')
}

# Initialize tape
tape = ['0', '1', '0', '1', '1', '0']

# Define initial state
state = 'A'

# Run the Universal Turing Machine (UTM) with the defined rules and initial state
while state != 'H':
    # Get current symbol
    symbol = tape[position]
    # Get current action based on symbol and state
    action = rules[(state, symbol)]
    # Update tape with new symbol
    tape[position] = action[1]
    # Move tape head left or right
    if action[2] == 'R':
        position += 1
    elif action[2] == 'L':
        position -= 1
    # Update state
    state = action[0]

# The machine eventually halts
```