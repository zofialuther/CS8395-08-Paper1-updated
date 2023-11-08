```python
# This is a Python environment, and the Java program cannot be directly translated to Python. However, we can create a similar program using the `list` data structure in Python to demonstrate the same stack operations.

# Creating a stack using list
stack = []

# Pushing elements onto the stack
stack.append("element1")
stack.append("element2")

# Checking if the stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

# Popping elements from the stack
popped_element = stack.pop()
print("Popped element:", popped_element)

# Example of popping from an empty stack
try:
    popped_element = stack.pop()
    print("Popped element:", popped_element)
except IndexError:
    print("Cannot pop from an empty stack")
```