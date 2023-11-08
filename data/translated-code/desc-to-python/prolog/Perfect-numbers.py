```python
def tt_divisors(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors)

def perfect(num):
    return tt_divisors(num) == num

def perfect_numbers(start, end):
    return [i for i in range(start, end+1) if perfect(i)]
```