```python
# Define lexer
def lexer(expression):
    # Tokenize the string into a list of tokens
    # Code for tokenizing the string goes here

# Define parser
def parser(tokens):
    # Construct an expression tree from the tokens
    # Code for constructing expression tree goes here

# Define evaluator
def evaluator(expression_tree):
    # Compute the value of the expression
    # Code for evaluating expression goes here

# Define main predicate calculator
def calculator(expression):
    tokens = lexer(expression)
    expression_tree = parser(tokens)
    result = evaluator(expression_tree)
    return result

# Example use of the calculator
result = calculator("3 + 4 * 2")
print(result)  # Output: 11
```