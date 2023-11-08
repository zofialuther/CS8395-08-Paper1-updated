```python
def is_happy(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit)**2 for digit in str(number))
    return number == 1

def happy_numbers():
    number = 1
    while True:
        if is_happy(number):
            yield number
        number += 1

def take(n, iterable):
    return [next(iterable) for _ in range(n)]

print(take(8, happy_numbers()))
```