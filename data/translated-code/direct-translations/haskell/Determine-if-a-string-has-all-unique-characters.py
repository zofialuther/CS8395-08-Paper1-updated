```python
import safe as S
import data.map.strict as M
from data.list import intercalate, foldl'
from data.ord import comparing
from numeric import showHex
from data.char import ord

def duplicatedCharIndices(xs):
    def go(a, i, c):
        if M.lookup(c, a) is None:
            a[c] = [i]
        else:
            a[c].append(i)
        return a

    char_map = foldl(go, {}, enumerate(xs))
    filtered_map = {k:v for k,v in char_map.items() if len(v) > 1}
    if len(filtered_map) == 0:
        return None
    min_char = min(filtered_map, key=lambda k: filtered_map[k][0])
    return (min_char, filtered_map[min_char])

def main():
    test_cases = ["", ".", "abcABC", "XYZ ZYX", "1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ"]
    result = [duplicatedCharIndices(x) for x in test_cases]
    print(result)

if __name__ == "__main__":
    main()
```