```python
def divisor_sum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def aliquot_sequence(n):
    sum = divisor_sum(n)
    if sum == n:
        return "perfect"
    elif sum == n and sum != 1:
        return "amicable"
    elif sum == n and sum == 1:
        return "sociable"
    elif sum > n:
        return "aspiring"
    elif sum == n and sum != 1:
        return "cyclic"
    else:
        return "non-terminating"

def write_aliquot_sequence(n):
    print(f"The aliquot sequence for {n} is {aliquot_sequence(n)}")

def main():
    numbers = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
    for number in numbers:
        write_aliquot_sequence(number)

main()
```