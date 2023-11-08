```python
def remove_last(s):
    return s[:-1]

def remove_first_last_chars(s):
    print("Original string:", s)
    print("String without first character:", s[1:])
    print("String without last character:", remove_last(s))
    print("String without first and last characters:", s[1:-1])

# Test the function
remove_first_last_chars("hello")
```