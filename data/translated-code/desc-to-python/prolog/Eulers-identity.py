```python
def simplify(expression):
    # define rules for simplifying mathematical expressions
    # including addition, multiplication, trigonometric functions, and special cases
    
def reduce(expression):
    result = simplify(expression)
    if result == expression:
        final_result = expression
    else:
        print(result)
        reduce(result)
```