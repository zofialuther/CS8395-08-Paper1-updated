from csp import CSP

problem = CSP()

variables = ['R2', 'R3', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'X', 'Y', 'Z']
for var in variables:
    problem.add_variable(var, list(range(152)))

# Add rules and constraints
# ...

# Iterate through possible solutions
solutions = problem.get_solution()
for solution in solutions:
    print("X:", solution['X'], "Y:", solution['Y'], "Z:", solution['Z'])