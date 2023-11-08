```python
import itertools

def brace_expansion(s):
    start = 0
    end = len(s)
    stack = []
    result = []

    for i, c in enumerate(s):
        if c == '{':
            stack.append(i)
        elif c == '}' and stack:
            if len(stack) == 1:
                start = stack.pop()
                options = s[start+1:i].split(',')
                end = i
                break

    prefix = s[:start]
    suffix = s[end+1:]

    for option in options:
        result.extend(brace_expansion(prefix + option + suffix))

    if not result:
        return [s]
    else:
        return result

print(brace_expansion("~/{Downloads,Pictures}/*.{jpg,gif,png}"))
print(brace_expansion("It{{em,alic}iz,erat}e{d,}, please."))
print(brace_expansion("{,{,gotta have{ ,\\, again\\, }}more }cowbell!"))
```