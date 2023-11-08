```python
import time

def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def dpa(limit):
    start_time = time.time()
    deficient = 0
    perfect = 0
    abundant = 0
    for num in range(1, limit+1):
        div_sum = sum(proper_divisors(num))
        if div_sum < num:
            deficient += 1
        elif div_sum == num:
            perfect += 1
        else:
            abundant += 1
    end_time = time.time()
    print(f"Deficient numbers: {deficient}")
    print(f"Perfect numbers: {perfect}")
    print(f"Abundant numbers: {abundant}")
    print(f"Time taken: {end_time - start_time} seconds")

dpa(1000)
```