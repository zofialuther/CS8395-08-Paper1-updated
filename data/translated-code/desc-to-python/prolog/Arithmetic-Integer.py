```python
def arithmetic_operations():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    integer_division = num1 // num2
    remainder_division = num1 % num2
    exponentiation = num1 ** num2

    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Integer Division:", integer_division)
    print("Remainder Division:", remainder_division)
    print("Exponentiation:", exponentiation)

    return True

arithmetic_operations()
```