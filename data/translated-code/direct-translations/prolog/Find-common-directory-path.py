```python
def directory_prefix(PATHs, STOP0, PREFIX):
    if not PATHs:
        return ''
    else:
        longest_prefix = longest_prefix(PATHs, STOP0, '')
        if longest_prefix:
            return PREFIX + STOP0 + longest_prefix
        else:
            return ''

def longest_prefix(PATHs, STOP0, PREFIX):
    for path in PATHs:
        if starts_with(path, PREFIX) and ends_with(PREFIX, STOP0):
            return PREFIX
    return ''

def shortest_prefix(PATHs, STOP0, PREFIX):
    if not PATHs:
        return PREFIX
    else:
        path0 = PATHs[0]
        if starts_with(path0, PREFIX) and ends_with(PREFIX, STOP0):
            return shortest_prefix(PATHs[1:], STOP0, PREFIX)
        else:
            return ''

def starts_with(TARGET, START):
    return TARGET.startswith(START)

def ends_with(TARGET, END):
    return TARGET.endswith(END)
```