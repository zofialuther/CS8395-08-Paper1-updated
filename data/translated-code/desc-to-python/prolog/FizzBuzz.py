```python
def fizzbuzz():
    for i in range(1, 101):
        print_item(i)

def print_item(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

fizzbuzz()
```