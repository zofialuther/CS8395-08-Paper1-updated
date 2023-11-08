```python
import random

def bnd(s):
    if s == "_##" or s == "#_#" or s == "##_":
        return '#'
    else:
        return '_'

def nxt(s):
    def go(x):
        if len(x) == 2:
            return None
        else:
            return (bnd(x[:3]), x[1:])
    return [bnd(s[i:i+3]) for i in range(len(s)-2)]

def lahmahgaan(xs):
    result = [xs]
    while result[-1] != nxt(result[-1]):
        result.append(nxt(result[-1]))
    return result

def main():
    random_nums = [random.choice("_#") for _ in range(36)]
    print('\n'.join(lahmahgaan(''.join(random_nums))))

if __name__ == "__main__":
    main()
```