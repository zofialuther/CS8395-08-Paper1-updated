```python
# Define a tuple of string class methods
string_methods = (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper)

# Iterate through each method in the tuple
for method in string_methods:
    # Generate a string of characters that satisfy the criteria of that method
    valid_chars = [c for c in map(chr, range(0, 256)) if method(c)]
    valid_chars_str = ''.join(valid_chars)

    # Print out the name of the method, the number of characters that meet the criteria, and the first 100 characters that satisfy the method
    print(method.__name__, len(valid_chars), valid_chars_str[:100])
```