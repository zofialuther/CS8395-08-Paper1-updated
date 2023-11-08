```python
def fusc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return fusc(n // 2)
    else:
        return fusc((n - 1) // 2) + fusc((n + 1) // 2)

fusc_numbers = [fusc(i) for i in range(61)]
max_length = 0
max_length_index = 0

for i, num in enumerate(fusc_numbers):
    if len(str(num)) > max_length:
        max_length = len(str(num))
        max_length_index = i

print(fusc_numbers)
print(f"The fusc number with the longest length is {fusc_numbers[max_length_index]} at index {max_length_index}")
```