```python
def runLengths(s):
    if s == "":
        return []
    else:
        def go(c, acc):
            if acc[0][0] == 0:
                return ((1, c), acc[1])
            else:
                n, x = acc[0]
                if c == x:
                    return ((n + 1, x), acc[1])
                else:
                    return ((1, c), (n, x) + acc[1])

        result = foldr(go, ((0, ' '), []), s)
        return [(n, c) for n, c in result[1]]

def main():
    testString = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWW" + "WWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = runLengths(testString)
    print(showLengths(encoded))
    print(all(map(lambda x: x[1]*x[0] == testString, encoded)))

def showLengths(lst):
    if lst == []:
        return ""
    else:
        n, c = lst[0]
        return str(n) + c + showLengths(lst[1:])
```