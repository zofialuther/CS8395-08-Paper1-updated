```python
def parse(s):
    return [list(map(int, line.split())) for line in s.split('\n')]

def f(a, b, c):
    return a + max(b, c)

def g(lst1, lst2):
    return [f(a, b, c) for a, b, c in zip(lst1, lst2)]

def solve(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(g(lst[i], lst[i + 1])[0])
    return result

with open('triangle.txt', 'r') as file:
    data = file.read()
    parsed_data = parse(data)
    result = solve(parsed_data)
    print(result)
```