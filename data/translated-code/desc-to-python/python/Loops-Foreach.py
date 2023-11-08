```python
# Create a dictionary
my_dict = {
    "b": 2,
    "a": 1,
    "c": 3
}

# Iterate through the dictionary keys in sorted order
for key in sorted(my_dict.keys()):
    print(f"{key}: {my_dict[key]}")
```