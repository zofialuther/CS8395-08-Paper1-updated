```python
def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def filter_even_numbers(nums):
    return [num for num in nums if is_even(num)]

def filter_odd_numbers(nums):
    return list(filter(is_odd, nums))

def filter_even_numbers_fold(nums):
    return list(filter(lambda x, y: x + [y] if is_even(y) else x, nums, []))

def main():
    numbers = list(range(1, 11))
    print("Even numbers:", filter_even_numbers(numbers))
    print("Odd numbers:", filter_odd_numbers(numbers))
    print("Even numbers using fold:", filter_even_numbers_fold(numbers))

def concatMap(func, lst):
    return [y for x in lst for y in func(x)]

def showReturn(func):
    return func.__code__.co_consts[0]

if __name__ == "__main__":
    main()
```