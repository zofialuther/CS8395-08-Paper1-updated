```python
# 1. Import necessary modules and language extensions
from parsec import *
import operator

# 2. Create a data type Exp with constructors for Num, Add, Sub, Mul, and Div
class Exp:
    def __init__(self, op, x, y):
        self.op = op
        self.x = x
        self.y = y

# 3. Define a function expr that takes a Stream and ParsecT and returns a parsed expression
def expr(s, pt):
    def op(x):
        return lambda y: Exp(x, s, y)
    table = [
        [op('*'), op('/')],
        [op('+'), op('-')]
    ]
    factor = choice([
        attempt(lazy(lambda: expr(s, pt))),
        number
    ])
    return buildExpressionParser(table, factor)

# 4. Define a function eval that takes an Exp and returns its evaluated value
def eval(exp):
    if exp.op == 'Num':
        return int(exp.x)
    elif exp.op == 'Add':
        return eval(exp.x) + eval(exp.y)
    elif exp.op == 'Sub':
        return eval(exp.x) - eval(exp.y)
    elif exp.op == 'Mul':
        return eval(exp.x) * eval(exp.y)
    elif exp.op == 'Div':
        return eval(exp.x) / eval(exp.y)

# 5. Define a function solution that takes a string and returns the evaluated expression
def solution(s):
    return eval(expr(s, pt).parse(s))

# 6. Define a main function that prints the result of solution for a given input string
def main():
    input_string = "3 + 4 * 2 / ( 1 - 5 )"
    print(solution(input_string))

main()
```