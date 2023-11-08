```python
# Initial data sets
setA = {"apple", "banana", "orange", "grape"}
setB = {"banana", "grape", "cherry", "pear"}

# Symmetric difference using union of differences
sym_diff1 = (setA - setB) | (setB - setA)

# Symmetric difference using union minus intersection
sym_diff2 = setA ^ setB

print("Initial setA:", setA)
print("Initial setB:", setB)
print("Symmetric difference using union of differences:", sym_diff1)
print("Symmetric difference using union minus intersection:", sym_diff2)
```