```python
def sum_of_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

def classify_numbers():
    deficient_count = 0
    perfect_count = 0
    abundant_count = 0
    for num in range(1, 20001):
        div_sum = sum_of_divisors(num)
        if div_sum < num:
            deficient_count += 1
        elif div_sum == num:
            perfect_count += 1
        else:
            abundant_count += 1
    print("Deficient numbers:", deficient_count)
    print("Perfect numbers:", perfect_count)
    print("Abundant numbers:", abundant_count)

classify_numbers()
```