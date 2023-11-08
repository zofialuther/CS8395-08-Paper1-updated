```python
numbers = []
coordinates = []

for num in range(10, 101, 10):
    numbers.append(num)
    x = num * 7
    y = (num * (num - 10)) + (num - 10)**2
    coordinates.append((x, y))

print(numbers)
print(coordinates)
```