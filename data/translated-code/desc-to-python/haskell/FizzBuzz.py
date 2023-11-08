```python
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

fizz_buzz_values = list(map(fizz_buzz, range(1, 101)))
for value in fizz_buzz_values:
    print(value)
```