```python
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def calculate_sequence(limit):
    sequence = []
    for i in range(1, limit+1):
        sequence.append(digit_sum(i) * digit_sum(i+1))
    return sequence

def create_table(sequence):
    print("Index\tValue")
    for i in range(len(sequence)):
        print(f"{i+1}\t{sequence[i]}")

sequence_values = calculate_sequence(40)
create_table(sequence_values)
```