```python
import math

def qmean(numbers):
    squares = [x**2 for x in numbers]
    sum_squares = sum(squares)
    mean = sum_squares / len(numbers)
    qmean = math.sqrt(mean)
    return qmean

numbers = list(range(1, 11))
result = qmean(numbers)
print(result)
```