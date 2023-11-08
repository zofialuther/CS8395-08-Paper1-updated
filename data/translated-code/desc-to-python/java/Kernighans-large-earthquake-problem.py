```python
# This functionality can be achieved in Python using the following code:

with open("data.txt", "r") as file:
    for line in file:
        components = line.split(",")
        magnitude = float(components[1])
        if magnitude > 6:
            print(line)
```