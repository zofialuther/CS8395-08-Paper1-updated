```python
def carpet(num):
    def weave(strings):
        def thread(s1, s2):
            return ''.join([a + b for a, b in zip(s1, s2)])
        
        def add_space(s):
            return ' ' + s + ' '
        
        return [''.join(map(add_space, s)) for s in strings]

    return '\n'.join(iterate(weave, ["██"], num))

def main():
    for i in range(3):
        print(carpet(i))
```