```python
# Define a lambda function for multiplication
multiply = lambda x, y: x * y

# Create a class "num" that inherits from the float class
class num(float):
    # Method for exponentiation using reduce function and the multiplication lambda
    def exponentiation(self, power):
        from functools import reduce
        return reduce(multiply, [self] * power, 1)

# Demonstrate the usage of exponentiation method
# With integer numbers
x = num(2)
print(x.exponentiation(3))  # Output: 8.0

# With float numbers
y = num(2.5)
print(y.exponentiation(2))  # Output: 6.25

# Using exponentiation as an operator
print(x ** 3)  # Output: 8.0
print(y ** 2)  # Output: 6.25
```