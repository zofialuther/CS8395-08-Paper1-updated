```python
from itertools import groupby

def look_and_say(n):
    return int(''.join(str(len(list(g))) + k for k, g in groupby(str(n))))

def main():
    sequence = [1]
    for _ in range(10):
        print(sequence[-1])
        sequence.append(look_and_say(sequence[-1]))

if __name__ == "__main__":
    main()
```