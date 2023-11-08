```python
def square(num):
    return num * num

numbers = [1, 3, 5, 7]

# Using list comprehension
squares_list_comprehension = [num*num for num in numbers]

# Using map function
squares_map_function = list(map(square, numbers))

# Using lambda function
squares_lambda_function = list(map(lambda x: x*x, numbers))

# Direct calculation
squares_direct_calculation = [1, 9, 25, 49]

# Using eager iterator
squares_eager_iterator = iter([num*num for num in numbers])

# Using lazy iterator
squares_lazy_iterator = (num*num for num in numbers)
```