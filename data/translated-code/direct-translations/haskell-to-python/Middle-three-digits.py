```python
def mid3(n):
    m = abs(n)
    s = str(m)
    lng = len(s)
    if m < 100:
        return "too small"
    elif lng % 2 == 0:
        return "even number of digits"
    else:
        return s[(lng - 3) // 2 : (lng - 3) // 2 + 3]

def main():
    xs = [123, 12345, 1234567, 987654321, 10001, -10001, -123, -100, 100, -12345, 1, 2, -1, -10, 2002, -2002, 0]
    w = max(len(str(x)) for x in xs)
    for n in xs:
        result = mid3(n)
        padding = " " * (w - len(str(n)))
        if isinstance(result, str):
            print(padding + str(n) + " -> " + result)
        else:
            print(padding + str(n) + " -> (" + result + ")")

def justifyRight(n, c, s):
    return (c * (n - len(s))) + s

if __name__ == "__main__":
    main()
```