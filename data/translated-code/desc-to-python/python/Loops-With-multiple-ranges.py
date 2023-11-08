```python
import itertools

def custom_range(start, stop, step):
    if step < 0:
        return list(itertools.islice(itertools.count(start, step), (start - stop) // step))
    else:
        return list(itertools.islice(itertools.count(start, step), (stop - start) // step))

product = 1
sum = 0
numbers = custom_range(1, 10, 2)

for num in numbers:
    product *= abs(num)
    sum += abs(num)

print("Product:", product)
print("Sum:", sum)
```