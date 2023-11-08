import itertools

# Define constraints as lambda functions with associated descriptions
constraints = (
    (lambda combo: combo[0] == True, "First statement must be true"),
    (lambda combo: combo[1] == False, "Second statement must be false"),
    # Define the rest of the constraints here
    # ...
)

# Generate all possible combinations of 12 true/false statements
combinations = list(itertools.product([True, False], repeat=12))

# Check each combination against the set of constraints
for combo in combinations:
    num_matches = 0
    unsatisfied_constraint = ""
    for constraint, description in constraints:
        if constraint(combo):
            num_matches += 1
        else:
            unsatisfied_constraint = description
    if num_matches == 12:
        print(combo, "Full match")
    elif num_matches == 11:
        print(combo, "Missed by one statement:", unsatisfied_constraint)