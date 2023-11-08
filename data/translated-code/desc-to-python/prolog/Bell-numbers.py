```python
def bell(n):
    bell_numbers = [0] * (n+1)
    bell_numbers[0] = 1
    for i in range(1, n+1):
        bell_numbers[i] = bell_numbers[i-1]
        for j in range(i-1, 0, -1):
            bell_numbers[j] += bell_numbers[j-1]
    return bell_numbers

def next_row(prev_row):
    new_row = [prev_row[-1]]
    for i in range(len(prev_row)):
        new_row.append(new_row[-1] + prev_row[i])
    return new_row[1:]

def print_bell_numbers(n):
    print(bell(n))

def print_bell_rows(n):
    row = [1]
    for i in range(n):
        print(row)
        row = next_row(row)

def main():
    print_bell_numbers(15)
    print(bell(50))
    print_bell_rows(10)

main()
```