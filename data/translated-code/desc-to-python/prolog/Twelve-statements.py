# Python code for logical puzzle

from constraint import *

problem = Problem()

# Add variables for each statement (s1, s2, ..., s12)
for i in range(1, 13):
    problem.addVariable('s' + str(i), [True, False])

# Add constraints for the truth values of the statements
problem.addConstraint(ExactSumConstraint(3), ['s7', 's8', 's9', 's10', 's11', 's12'])
problem.addConstraint(ExactSumConstraint(2), ['s2', 's4', 's6', 's8', 's10', 's12'])
# Add more constraints...

# Use constraint solver to determine the truth values of the statements
solutions = problem.getSolutions()

# Output the result
print(solutions)