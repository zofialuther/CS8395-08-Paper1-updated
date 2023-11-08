```python
# Python code to generate and print the first 10 terms of Van Eck's sequence, as well as terms 991 to 1000

def van_eck(first_index, last_index):
    sequence = [0] * (last_index + 1)
    last_seen = {}
    for i in range(1, last_index + 1):
        if sequence[i-1] not in last_seen:
            sequence[i] = 0
        else:
            sequence[i] = i - 1 - last_seen[sequence[i-1]]
        last_seen[sequence[i-1]] = i - 1
    for j in range(first_index, last_index + 1):
        print(sequence[j])
        
van_eck(1, 10)
van_eck(991, 1000)
```