import ast

# Parse the initial expression
expr = "2 * (3 - 1) + 2 * 5"
parsed_expr = ast.parse(expr, mode='eval')

# Print the resulting AST
print(ast.dump(parsed_expr))

# Compile the parsed expression into a code object
code = compile(parsed_expr, '<string>', 'eval')

# Evaluate the expression
result = eval(code)
print(result)

# Modify the AST
ast.fix_missing_locations(parsed_expr)
parsed_expr.body.right = ast.Num(6)

# Compile the modified AST into a new code object
modified_code = compile(parsed_expr, '<string>', 'eval')

# Evaluate the modified expression
modified_result = eval(modified_code)
print(modified_result)