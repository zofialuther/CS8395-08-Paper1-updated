```python
# Python does not have a built-in Scanner class, so we can use the input() function instead
m = int(input("Enter the first value: "))
n = int(input("Enter the second value: "))

# Function to calculate the LCM
def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

# Display the calculated LCM
print("The least common multiple of", m, "and", n, "is", calculate_lcm(m, n))
```