```python
import itertools

expression = input("Enter a boolean expression: ")

variables = list(set([char for char in expression if char.isalpha()]))
combinations = list(itertools.product([True, False], repeat=len(variables)))

for combo in combinations:
    mapping = {variables[i]: combo[i] for i in range(len(variables))}
    truth_value = eval(expression, mapping)
    print(mapping, truth_value)
```