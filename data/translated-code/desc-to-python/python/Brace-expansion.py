def getgroup(s, start):
    count = 1
    i = start + 1
    while count > 0:
        if s[i] == '{':
            count += 1
        elif s[i] == '}':
            count -= 1
        i += 1
    return s[start:i]

def getitem(s, depth=0):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '{':
            result.append(getgroup(s, i))
            i += len(result[-1])
        i += 1
    return result

# Sample usage
strings = ["{a, b, c}", "{1, 2, {3, 4}, {5, 6}}", "{{x, y}, z}"]
for string in strings:
    print(getitem(string))