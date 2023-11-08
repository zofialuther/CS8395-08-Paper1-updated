```python
import random

def play24(Len, Range, Goal):
    expressions = game(Len, Range, Goal)
    for exp, result in expressions:
        my_write(exp, result)

def game(Len, Range, Goal):
    numbers = [random.randint(1, Range) for _ in range(Len)]
    expressions = []
    for i in range(len(numbers)):
        compute(numbers[i], [numbers[j] for j in range(len(numbers)) if j != i], str(numbers[i]), expressions, Goal)
    return expressions

def compute(num, rest, exp, expressions, Goal):
    if len(rest) == 0:
        if num == Goal:
            expressions.append((exp, num))
        return
    for i in range(len(rest)):
        compute(num + rest[i], [rest[j] for j in range(len(rest)) if j != i], exp + "+" + str(rest[i]), expressions, Goal)
        compute(num - rest[i], [rest[j] for j in range(len(rest)) if j != i], exp + "-" + str(rest[i]), expressions, Goal)
        compute(num * rest[i], [rest[j] for j in range(len(rest)) if j != i], exp + "*" + str(rest[i]), expressions, Goal)
        if rest[i] != 0 and num % rest[i] == 0:
            compute(num / rest[i], [rest[j] for j in range(len(rest)) if j != i], exp + "/" + str(rest[i]), expressions, Goal)

def my_write(exp, result):
    print(exp + " = " + str(result))
```