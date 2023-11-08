```python
# Get the 2 numbers from command line arguments
a = int(input())
b = int(input())

sum = a + b  # The result of adding 'a' and 'b' (Note: integer addition is discouraged in print statements due to confusion with string concatenation)
difference = a - b  # The result of subtracting 'b' from 'a'
product = a * b  # The result of multiplying 'a' and 'b'
division = a // b  # The result of dividing 'a' by 'b' (Note: 'division' does not contain the fractional result)
remainder = a % b  # The remainder of dividing 'a' by 'b'

print("a + b = " + str(sum))
print("a - b = " + str(difference))
print("a * b = " + str(product))
print("quotient of a / b = " + str(division))  # truncates towards 0
print("remainder of a / b = " + str(remainder))  # same sign as first operand
```