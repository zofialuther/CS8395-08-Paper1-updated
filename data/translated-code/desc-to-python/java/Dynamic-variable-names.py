```python
# Python code

# Create an empty dictionary to store variables and values
variable_map = {}

# Use input() function to accept user input for variable names and values
variable_name = input("Enter variable name: ")
variable_value = input("Enter variable value: ")

# Store the variable and value in the dictionary
variable_map[variable_name] = variable_value

# Retrieve the value of a variable using its name as key
print(variable_map[variable_name])
```