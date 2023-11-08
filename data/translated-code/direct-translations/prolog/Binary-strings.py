```python
# Create a string (no destruction necessary)
# X = "a test string".
X = "a test string"

# String assignment, there is no assignment but you can unify between variables, also 'String cloning and copying'
# X = "a test string", X = Y.
X = "a test string"
Y = X

# String comparison
# X = "a test string", Y = "a test string", X = Y.
X = "a test string"
Y = "a test string"
X == Y

# X = "a test string", Y = "a different string", X = Y.
X = "a test string"
Y = "a different string"
X == Y

# Test for empty string, this is the same as string comparison.
# X = "a test string", Y = "", X = Y.
X = "a test string"
Y = ""
X == Y

# X = "", Y = "", X = Y.
X = ""
Y = ""
X == Y

# Append a byte to a string
# X = "a test string", string_concat(X, "!", Y).
X = "a test string"
Y = X + "!"

# Extract a substring from a string
# X = "a test string", sub_string(X, 2, 4, _, Y).
X = "a test string"
Y = X[1:5]

# X = "a test string", sub_string(X, Before, Len, After, test).
X = "a test string"
Before = X.find("test") + 1
Len = len("test")
After = len(X) - Before - Len

# Replace every occurrence of a byte (or a string) in a string with another string
# X = "a test string", re_replace('t'/g, 'o', X, Y).
import re
X = "a test string"
Y = re.sub('t', 'o', X)

# Join strings
# X = "a test string", Y = " with extra!", string_concat(X, Y, Z).
X = "a test string"
Y = " with extra!"
Z = X + Y
```