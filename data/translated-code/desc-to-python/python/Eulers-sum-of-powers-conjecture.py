```python
# Create a dictionary to store i^5 + j^5 values
pairs = {}

# Iterate through the range of 1 to 250 and store i^5 + j^5 values in the dictionary
for i in range(1, 251):
    for j in range(1, 251):
        result = i**5 + j**5
        if result in pairs:
            pairs[result].append((i, j))
        else:
            pairs[result] = [(i, j)]

# Iterate through the dictionary to find pairs that satisfy the condition
for key, value in pairs.items():
    if len(value) > 1:
        print(f"Pairs for {key}: {value}")

# Exit the program
exit()
```