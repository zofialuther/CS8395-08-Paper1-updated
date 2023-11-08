```python
def proper_divisors(num):
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return divisors

def show_proper_divisors_of_range(start, end):
    for i in range(start, end+1):
        divisors = proper_divisors(i)
        print(f"{i}:{divisors}")

def find_most_proper_divisors_in_range(start, end):
    max_divisors = 0
    num_with_max_divisors = 0
    for i in range(start, end+1):
        divisors = proper_divisors(i)
        if len(divisors) > max_divisors:
            max_divisors = len(divisors)
            num_with_max_divisors = i
    return f"Result = num({num_with_max_divisors})-divisor_count({max_divisors})"

# Test the functions
show_proper_divisors_of_range(1, 10)
print(find_most_proper_divisors_in_range(1, 20000))
```