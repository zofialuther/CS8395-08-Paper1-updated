```python
import itertools

def dept(x):
    return x in range(1, 8)

def police(x):
    return x in [1, 3, 5]

def fire(x):
    return dept(x)

def san(x):
    return dept(x)

def assign(p, f, s):
    return p != f and p != s and f != s and p + f + s == 12

def main():
    departments = list(range(1, 8))
    valid_combinations = [(p, f, s) for p, f, s in itertools.product(departments, departments, departments) if assign(p, f, s)]
    for combo in valid_combinations:
        print(combo)

main()
```