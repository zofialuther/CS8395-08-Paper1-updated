```python
def arithmetic(x, y):
    operators = ['+', '-', '*', '//', '%', '**']
    for operator in operators:
        expression = "{x} {op} {y}".format(x=x, op=operator, y=y)
        result = eval(expression)
        print(expression, "=", result)

arithmetic(12, 8)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
arithmetic(num1, num2)
```