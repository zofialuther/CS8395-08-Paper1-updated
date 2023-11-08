```python
def is_narcissistic(num):
    num_str = str(num)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    return total == num

count = 0
num = 0
while count < 25:
    if is_narcissistic(num):
        print(num)
        count += 1
    num += 1
```