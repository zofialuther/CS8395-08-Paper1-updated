```python
from big_rational import BigRational

def is_perfect_number(num):
    reciprocal_sum = BigRational(0)
    for i in range(1, num):
        if num % i == 0:
            reciprocal_sum += BigRational(1, i)
    return reciprocal_sum == BigRational(2)

def find_perfect_numbers(start, end):
    for num in range(start, end+1):
        if is_perfect_number(num):
            print(num)

find_perfect_numbers(1, 524287)
```