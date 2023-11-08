def evaluate_truth_table(expression):
    # Step 1: Tokenize the input
    tokens = tokenize(expression)
    
    # Step 2: Convert it into an evaluatable term
    term = convert_to_term(tokens)
    
    # Step 3: Evaluate the expression for each permutation of variables
    variable_permutations = generate_variable_permutations(get_variables(expression))
    
    print_truth_table(variable_permutations, term)
    
def tokenize(expression):
    # code for tokenizing the input
    pass

def convert_to_term(tokens):
    # code for converting tokens into evaluatable term
    pass

def get_variables(expression):
    # code for extracting variables from the expression
    pass

def generate_variable_permutations(variables):
    # code for generating permutations of variable values
    pass

def print_truth_table(variable_permutations, term):
    # code for printing truth table
    pass

# Example usage
evaluate_truth_table("((A and B) or (not C))")