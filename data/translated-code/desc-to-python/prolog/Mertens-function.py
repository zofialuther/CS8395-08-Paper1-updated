```python
def mertens_number(n):
    if n == 1:
        return 1
    else:
        return mertens_number(n-1) - sum(mertens_number(n-1) for n in range(1, n))

def print_mertens_numbers():
    for i in range(1, 200):
        print(mertens_number(i))

def count_zero_crossings(start, end):
    count_crossings = 0
    count_equals_zero = 0
    prev_value = mertens_number(start)
    for i in range(start+1, end+1):
        current_value = mertens_number(i)
        if prev_value * current_value < 0:
            count_crossings += 1
        if current_value == 0:
            count_equals_zero += 1
        prev_value = current_value
    print(f"Number of zero crossings: {count_crossings}")
    print(f"Number of times equals zero: {count_equals_zero}")

print_mertens_numbers()
count_zero_crossings(1, 100)
```