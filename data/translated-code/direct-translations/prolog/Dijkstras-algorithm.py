```python
from collections import defaultdict

edges = defaultdict(dict)
edges['a']['b'] = 7
edges['a']['c'] = 9
edges['b']['c'] = 10
edges['b']['d'] = 15
edges['c']['d'] = 11
edges['d']['e'] = 6
edges['a']['f'] = 14
edges['c']['f'] = 2
edges['e']['f'] = 9

rpath = {}

def path(From, To, Dist):
    return To in edges[From]

def shorterPath(Path, Dist):
    global rpath
    if Path[0] in rpath and Dist < rpath[Path[0]]:
        rpath[Path[0]] = Dist
        print(f"{Path} is closer than {rpath[Path[0]]}")
    else:
        print(f"New path: {Path}")
        rpath[Path[0]] = Dist

def traverse(From, Path=[], Dist=0):
    for T, D in edges[From].items():
        if T not in Path:
            shorterPath([T, From] + Path, Dist + D)
            traverse(T, [From] + Path, Dist + D)

def go(From, To):
    traverse(From)
    if To in rpath:
        Path = [To] + [node for node in rpath.keys() if rpath[node] <= rpath[To]]
        Path.reverse()
        Distance = round(rpath[To])
        print(f"Shortest path is {Path} with distance {rpath[To]} = {Distance}")
    else:
        print(f"There is no route from {From} to {To}")
```