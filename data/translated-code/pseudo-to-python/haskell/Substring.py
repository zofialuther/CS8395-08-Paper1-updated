```python
def fromMforN(n, m, s):
    return s[n:n+m]

def fromNtoEnd(n, s):
    return s[n:]

def allButLast(s):
    return s[:-1]

def fromCharForN(m, needle, haystack):
    return haystack[haystack.index(needle):haystack.index(needle) + m]

def fromStringForN(m, needle, haystack):
    return haystack[haystack.index(needle):haystack.index(needle) + m]

def main():
    strings = ["天地不仁仁者人也🐒话说天下大势分久必合🍑合久必分🔥"]
    list(map(print, [
        fromMforN(9, 10, strings[0]),
        fromNtoEnd(20, strings[0]),
        allButLast(strings[0]),
        fromCharForN(6, "话", strings[0]),
        fromStringForN(6, "大势", strings[0])
    ]))
```