```python
# Creating a string
string = "Hello, World!"

# String assignment and comparison
string1 = "Hello"
string2 = "World"
if string1 == string2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# Testing for empty strings
if not string1:
    print("String1 is empty")
else:
    print("String1 is not empty")

# Appending a byte to a string
string += " How are you?"

# Extracting a substring
substring = string[7:12]

# Replacing occurrences of a byte or string in a string
new_string = string.replace("Hello", "Hi")

# Joining strings together
new_string = string1 + " " + string2
```