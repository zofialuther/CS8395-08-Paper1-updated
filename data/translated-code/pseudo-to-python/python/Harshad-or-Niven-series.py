```python
import itertools

def harshad():
    n = 1
    while True:
        if n % sum_of_digits(n) == 0:
            yield n
        n += 1

def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

harshad_numbers = list(itertools.islice(harshad(), 0, 20))
print(harshad_numbers)

for n in harshad():
    if n > 1000:
        print(n)
        break
```