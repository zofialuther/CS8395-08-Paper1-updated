```python
def quibbles(s):
    return "{" + s + "}"

def quibble(lst):
    return "".join(map(quibbles, lst))

def main():
    input_lists = [[], ["hello"], ["apple", "banana", "cherry"], "hello world".split(), "python is fun".split()]
    mapM_(print, map(quibble, input_lists))

main()
```