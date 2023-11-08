```python
def sumDigits(number, base):
    if base < 2:
        return "Error: Base must be at least 2"
    
    total = 0
    number = abs(number)
    while number > 0:
        total += number % base
        number //= base
    
    return total

# Example calls
print(sumDigits(123, 10))  # Output: 6
print(sumDigits(1010, 2))  # Output: 2
print(sumDigits(777, 8))  # Output: 21
```