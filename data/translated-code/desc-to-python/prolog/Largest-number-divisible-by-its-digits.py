```python
# Import the necessary library for generating permutations
from itertools import permutations

# Function to calculate the least common multiple of a list of numbers
def lcm(a, b):
    # Calculate the greatest common divisor
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    # Return the least common multiple using the formula
    return a * b // gcd(a, b)

# Generate all permutations of the digits 1 to 9
perms = permutations('123456789')

# Iterate through the permutations in reverse order
for perm in reversed(list(perms)):
    # Convert the permutation to an integer
    num = int(''.join(perm))
    # Calculate the least common multiple of all digits in the number
    l = 1
    for d in map(int, perm):
        l = lcm(l, d)
    # Check if the number is divisible by the least common multiple
    if num % l == 0:
        print(num)
        break
```