```python
# Define a dictionary to store the relationships between teachers and students
relationships = {
    "Socrates": "Plato"
}

# Define a function to check if a person is a student of another person
def student(X, Y):
    if X in relationships and relationships[X] == Y:
        return True
    else:
        return False

# Test the student function
print(student("Plato", "Socrates"))  # Output: False
print(student("Plato", "Socrates"))  # Output: True
```