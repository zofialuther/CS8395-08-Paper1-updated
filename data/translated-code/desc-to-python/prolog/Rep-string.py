```python
from functional import seq

def repstring(s):
    return seq.range(1, len(s)).flat_map(lambda i: seq.range(0, len(s) - i).map(lambda j: s[j:j + i])).group_by(lambda x: x).filter(lambda x: len(x[1]) > 1).map(lambda x: x[0])

def test_for_repstring(s):
    substrings = repstring(s)
    if substrings:
        return (s, True, substrings)
    else:
        return (s, False, [])

def test_strings(strings):
    return seq(strings).map(test_for_repstring)

def report_repstring(result):
    if result[1]:
        print(f"String: {result[0]}, Repeated Substrings: {result[2]}")
    else:
        print(f"String: {result[0]}, No repeated substrings found")

def report_repstrings(strings):
    seq(strings).map(test_for_repstring).for_each(report_repstring)
```