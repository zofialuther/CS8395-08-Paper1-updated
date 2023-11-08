```python
def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.extend([i, n//i])
    return list(set(divisors))

def count_proper_divisors(n):
    return len(proper_divisors(n))

def format_result(n, divisors):
    return f"The number {n} has {len(divisors)} proper divisors: {divisors}"

def show_count(limit):
    max_divisors = 0
    max_number = 0
    for i in range(1, limit+1):
        divisors = proper_divisors(i)
        if len(divisors) > max_divisors:
            max_divisors = len(divisors)
            max_number = i
    print(format_result(max_number, proper_divisors(max_number)))

for i in range(1, 101):
    print(f"The proper divisors of {i} are {proper_divisors(i)}")

show_count(100)

show_count(20000)
show_count(25000)
```