```python
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def hailstone(n):
    sequence = [n]
    while n != 1:
        n = collatz(n)
        sequence.append(n)
    return sequence

def longestChain():
    max_length = 0
    starting_number = 0
    for i in range(1, 100001):
        sequence_length = len(hailstone(i))
        if sequence_length > max_length:
            max_length = sequence_length
            starting_number = i
    return starting_number

def main():
    print(hailstone(27))
    print(longestChain())
    print(len(hailstone(longestChain())))

main()
```