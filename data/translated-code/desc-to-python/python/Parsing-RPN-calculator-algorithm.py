```python
# Create dictionary of mathematical operations and lambda functions
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

# String of numbers and operators
input_string = "5+3*2-6/2"

# Initialize list to store results
results = []

# Initialize current number
current_num = 0

# Iterate through input string
for char in input_string:
    if char.isdigit():
        current_num = current_num * 10 + int(char)
    else:
        results.append(current_num)
        current_num = 0
        if char in operations:
            results.append(char)
        else:
            print("Invalid operator:", char)
    print("Current operation:", char, "Resulting list:", results)

# Append final number to results
results.append(current_num)

# Print final resulting list
print("Final resulting list:", results)
```