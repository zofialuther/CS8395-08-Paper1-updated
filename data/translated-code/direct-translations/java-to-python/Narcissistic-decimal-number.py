```python
numbers_to_calculate = 25
numbers_calculated = 0

def is_narcissistic_number(num):
    length = len(str(num))
    added_digits = 0

    for digit in str(num):
        value = int(digit)
        added_digits += value ** length

    if num == added_digits:
        return True
    else:
        return False

for i in range(10**10):
    if is_narcissistic_number(i):
        numbers_calculated += 1
        print(i, end=" ")
    
    if numbers_calculated == numbers_to_calculate:
        break
```