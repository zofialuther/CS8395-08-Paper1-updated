```python
# Create a string
X = "a test string"

# String assignment
X = "a test string"
Y = X

# String comparison
X = "a test string"
Y = "a test string"
X = Y

X = "a test string"
Y = "a different string"
X != Y

# Test for empty string
X = "a test string"
Y = ""
X != Y

X = ""
Y = ""
X != Y

# Append a byte to a string
X = "a test string"
Y = X + "!"
Y = "a test string!"

# Extract a substring from a string
X = "a test string"
Y = X[2:6]
Y = "test"

X = "a test string"
Before = X.find("test")
Len = len("test")
After = Before + Len

# Replace every occurrence of a byte in a string with another string
X = "a test string"
Y = X.replace('t', 'o')
Y = "a oeso so ring"

# Join strings
X = "a test string"
Y = " with extra!"
Z = X + Y
Z = "a test string with extra!"
```