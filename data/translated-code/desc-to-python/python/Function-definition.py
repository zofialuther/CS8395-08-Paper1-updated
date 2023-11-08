```python
class Multiply:
    def __call__(self, x, y):
        return x * y

multiply = Multiply()
result = multiply(2, 4)
print(result)
```