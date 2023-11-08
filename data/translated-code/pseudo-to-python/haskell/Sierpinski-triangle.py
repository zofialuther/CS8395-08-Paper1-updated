```python
from itertools import accumulate, islice, chain

def sierpinski(num):
    def next(char):
        return "".join(map(lambda x, y: (' ' != x) ^ (' ' != y), ' ' + char, char + ' '))
    rule90 = accumulate(chain([1], range(2, num)), next)
    
    def spacing(x, sw):
        s, w = sw
        return (w + ' '.join(x) + '\n' + s, w != ' ')
    
    return rule90(2 ** num - 1 + 1)[1][0]

def main():
    print(sierpinski(4))

main()
```