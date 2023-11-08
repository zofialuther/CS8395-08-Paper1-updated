```python
import random

links = [
    [2, 3, 4],
    [3, 4, 5],
    [2, 4],
    [5],
    [2, 3, 4],
    [3, 4, 5]
]

pegs = [0] * 8

def main():
    vals = list(range(1, 9))
    while True:
        random.shuffle(vals)
        for i in range(8):
            pegs[i] = vals[i]
        if solved():
            break
    printResult()

def solved():
    for i in range(len(links)):
        for peg in links[i]:
            if abs(pegs[i] - peg) == 1:
                return False
    return True

def printResult():
    print("  {} {}\n{} {} {} {}\n  {} {}".format(pegs[0], pegs[1], pegs[2], pegs[3], pegs[4], pegs[5], pegs[6], pegs[7]))

main()
```