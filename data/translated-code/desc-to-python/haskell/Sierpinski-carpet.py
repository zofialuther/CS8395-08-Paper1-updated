```python
def weave(lst):
    return ["".join(x) for x in zip(lst[0], lst[1])]

def carpet(n):
    return "\n".join(iterate(weave, ["██"], n))

def iterate(func, initial, n):
    result = initial
    for i in range(n):
        result = func(result)
    return result

def main():
    print(carpet(5))

main()
```