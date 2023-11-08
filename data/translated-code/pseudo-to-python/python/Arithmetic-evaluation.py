import ast

expression = "2 * (3 - 1) + 2 * 5"
node = ast.parse(expression, mode='eval')
print(ast.dump(node).replace(',', '\n'))

code_object = compile(node, filename='<string>', mode='eval')
print(eval(code_object))

new_expression = "2 * (3 - 1) + 2 * 6"
new_node = ast.parse(new_expression, mode='eval')
new_code_object = compile(new_node, filename='<string>', mode='eval')
print(eval(new_code_object))