```python
def power_of_4_greater_than(num):
    power = 1
    while 4 ** power <= num:
        power += 1
    return 4 ** power

def integer_square_root(num):
    return int(num ** 0.5)

def display_integer_square_roots(start, end):
    for i in range(start, end+1):
        print(f"Integer square root of {i}: {integer_square_root(i)}")

# Example usage
num = 25
print(f"Power of 4 greater than {num}: {power_of_4_greater_than(num)}")

display_integer_square_roots(1, 10)
```