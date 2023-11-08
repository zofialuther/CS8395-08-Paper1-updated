import itertools

def brace_expansion(s):
    parts = [[]]
    for c in s:
        if c == '{':
            parts[-1].append('')
            parts.append([])
        elif c == '}':
            temp = parts.pop()
            parts[-1] = [x + y for x in parts[-1] for y in temp]
        elif c == ',':
            parts[-1].append('')
        else:
            for part in parts:
                part[-1] += c
    return parts[0]

print(brace_expansion("~/{Downloads,Pictures}/*.{jpg,gif,png}"))
print(brace_expansion("It{{em,alic}iz,erat}e{d,}, please."))
print(brace_expansion("{,{,gotta have{ ,\\, again\\, }}more }cowbell!"))