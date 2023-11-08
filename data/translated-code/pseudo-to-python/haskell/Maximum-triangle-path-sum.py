```python
def parse(s):
    return list(map(lambda x: list(map(int, x.split())), s.split('\n')))

def f(x, y, z):
    return x + max(y, z)

def g(xs, ys):
    return [f(x, y, z) for x, y, z in zip(xs, ys, ys[1:])]

def solve(triangle):
    return triangle[0][0] + max(reduce(g, triangle[1:]))

with open('triangle.txt', 'r') as file:
    contents = file.read()
    result = solve(parse(contents))
    print(result)
```