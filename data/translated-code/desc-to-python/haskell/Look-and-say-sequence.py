```python
from itertools import groupby

def lookAndSay(n):
    return int(''.join(str(len(list(g))) + k for k, g in groupby(str(n))))

def lookAndSay2(n):
    return int(''.join(str(len(list(g))) + k for k, g in groupby(str(n))))

def lookAndSay3(n):
    return int(''.join(str(len(list(g))) + k for k, g in groupby(str(n))))

def main():
    sequence = [1]
    for _ in range(10):
        sequence.append(lookAndSay(sequence[-1]))
    print(sequence)

if __name__ == "__main__":
    main()
```