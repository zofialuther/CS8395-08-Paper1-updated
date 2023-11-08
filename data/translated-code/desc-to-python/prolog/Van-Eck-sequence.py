```python
def van_eck_sequence():
    sequence = [0]
    last_seen = {0: 0}
    for i in range(1, 1001):
        if sequence[-1] in last_seen:
            sequence.append(i - 1 - last_seen[sequence[-1]])
        else:
            sequence.append(0)
        last_seen[sequence[-2]] = i - 1
    return sequence

def display_sequence(sequence, start, end):
    print(sequence[start:end])

van_eck = van_eck_sequence()
display_sequence(van_eck, 0, 10)
display_sequence(van_eck, 990, 1000)
```