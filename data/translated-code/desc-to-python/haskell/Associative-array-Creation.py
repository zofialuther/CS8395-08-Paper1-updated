```python
# Create a dictionary
my_dictionary = {
  "key1": "val1",
  "key2": "val2",
  "key3": "val3"
}

# Define lookup function
def lookup(dictionary, key):
  if key in dictionary:
    return Just(dictionary[key])
  else:
    return Nothing

# Use lookup function
result = lookup(my_dictionary, "key2")
```