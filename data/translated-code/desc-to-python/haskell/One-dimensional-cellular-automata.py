```python
import random

def bnd(char):
    if char in ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y']:
        return '#'
    else:
        return '_'

def nxt(s):
    return ''.join([bnd(char) for char in s])

def lahmahgaan(s):
    strings = [s]
    while len(strings) < 10: # Replace 10 with the desired condition
        s = nxt(s)
        strings.append(s)
    return strings

def main():
    initial_string = ''.join(random.choice(['a', 'b']) for _ in range(36))
    strings = lahmahgaan(initial_string)
    for string in strings:
        print(string)

main()
```