```python
def f(n, (a, b)):
    new_tuple = (2 * n, (a**2 + b**2, 2*a*b + b**2))
    return new_tuple

# Example of iteration
result = (1, (0, 1))
for i in range(5):
    result = f(i, result)
print(result[1])
```