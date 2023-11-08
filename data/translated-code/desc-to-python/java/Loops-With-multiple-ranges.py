```python
def calculate_power(base, exponent):
    return base ** exponent

numbers = []
for i in range(1, 6):
    for j in range(1, 4):
        numbers.append(i * j)

sum_of_numbers = sum([abs(num) for num in numbers])
product_of_nonzero = 1
for num in numbers:
    if num != 0:
        product_of_nonzero *= num

print("Sum of numbers:", sum_of_numbers)
print("Product of non-zero numbers:", product_of_nonzero)
print("List of numbers:", numbers)
```