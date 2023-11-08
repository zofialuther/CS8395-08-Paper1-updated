```python
def tail(lst):
    return lst[1:]

def init(lst):
    return lst[:-1]

def ap(f, args):
    return [f(arg) for arg in args]

def chunksOf(size, lst):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def compose(f, g):
    return lambda x: f(g(x))

def transpose(lst):
    return list(map(list, zip(*lst)))

def main():
    strings = ["abc", "def", "ghi"]
    transposed = transpose(strings)
    for row in transposed:
        print("".join(row))

main()
```