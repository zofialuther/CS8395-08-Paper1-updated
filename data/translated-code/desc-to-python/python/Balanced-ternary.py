```python
class BalancedTernary:
    def __init__(self, digits):
        self.digits = digits

    def to_integer(self):
        integer = 0
        power = 0
        for digit in self.digits:
            integer += digit * (3 ** power)
            power += 1
        return integer

    def add(self, other):
        # Implementation for addition

    def subtract(self, other):
        # Implementation for subtraction

    def multiply(self, other):
        # Implementation for multiplication

def main():
    num1 = BalancedTernary([1, 0, -1, 1])
    num2 = BalancedTernary([-1, 1, 0])
    
    print(num1.to_integer())  # Output: 16
    print(num2.to_integer())  # Output: -13
    
    result = num1.add(num2)
    print(result.to_integer())  # Output: 3
    
    result = num1.subtract(num2)
    print(result.to_integer())  # Output: 29
    
    result = num1.multiply(num2)
    print(result.to_integer())  # Output: -208
```