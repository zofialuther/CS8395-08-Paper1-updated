```python
# Python equivalent of the given Java program FourSquares
# Assuming the specified range for a, b, c, d, e, f, and g is 1 to 10

unique_solutions = set()
non_unique_solutions = set()

for a in range(1, 11):
    for b in range(1, 11):
        for c in range(1, 11):
            for d in range(1, 11):
                for e in range(1, 11):
                    for f in range(1, 11):
                        for g in range(1, 11):
                            combination = (a, b, c, d, e, f, g)
                            if len(set(combination)) == len(combination):
                                # Check for uniqueness
                                unique_solutions.add(combination)
                            else:
                                non_unique_solutions.add(combination)

print("Unique solutions:", len(unique_solutions))
print("Non-unique solutions:", len(non_unique_solutions))
```