```python
# Python code

# Importing libraries
import itertools

# Function for evaluating the token sequence in a given context
def evaluate_expression(expression, context):
    # Implementation of evaluating the expression
    pass

# Function for pretty printing the truth table
def print_truth_table(variables, truth_values):
    # Implementation of printing the truth table
    pass

# Main function
def main():
    # Reading input logical expression from the user
    expression = input("Enter a logical expression: ")
    
    # Generating all possible combinations of variables
    variables = list(expression)  # Assuming variables are single characters
    possible_combinations = list(itertools.product([True, False], repeat=len(variables))
    
    # Calculating truth values for all possible combinations of variables
    truth_values = [evaluate_expression(expression, dict(zip(variables, combo))) for combo in possible_combinations]
    
    # Printing the corresponding truth table
    print_truth_table(variables, truth_values)

# Calling the main function
main()
```