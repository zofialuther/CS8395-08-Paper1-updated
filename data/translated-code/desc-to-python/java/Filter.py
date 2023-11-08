```python
original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in original_array:
    if num % 2 == 0:
        evens.append(num)

evens = list(evens)
```