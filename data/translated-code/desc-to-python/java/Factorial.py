```python
def calculate_factorial(num):
    if num < 0:
        return "Error: Input must be a non-negative integer"
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

valid_input = False
while not valid_input:
    try:
        user_input = int(input("Enter a non-negative integer: "))
        if user_input >= 0:
            valid_input = True
        else:
            print("Error: Input must be a non-negative integer")
    except ValueError:
        print("Error: Input must be a non-negative integer")

result = calculate_factorial(user_input)
print(f"The factorial of {user_input} is {result}")
```