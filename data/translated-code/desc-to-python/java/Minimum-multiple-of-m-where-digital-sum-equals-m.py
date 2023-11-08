```python
def digitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

min_sum = float('inf')
for i in range(1, 71):
    current_sum = digitSum(i)
    if current_sum < min_sum:
        min_sum = current_sum

print("The minimum multiple digit sum for numbers from 1 to 70 is:", min_sum)
```