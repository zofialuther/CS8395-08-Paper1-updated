```python
def divisor(n):
    return [x for x in range(1, n) if n % x == 0]

def reciprocation(divisors):
    return [1/x for x in divisors]

def is_perfect(n):
    return sum(reciprocation(divisor(n))) == n

def find_perfect_numbers(limit):
    perfect_numbers = []
    for i in range(1, limit):
        if is_perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers

print(find_perfect_numbers(10000))
```