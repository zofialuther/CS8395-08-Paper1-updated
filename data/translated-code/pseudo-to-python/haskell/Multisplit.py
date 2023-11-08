def multisplit(delims, input):
    acc = []
    pos = 0
    while input:
        result = trysplit(delims, input)
        if result is None:
            acc.append(input)
            pos += 1
            input = input[1:]
        else:
            d, sxx = result
            acc, d, pos = (acc, d, pos)
            pos += len(d)
            input = sxx
    return [(acc, [], pos)]

def trysplit(delims, s):
    for d in delims:
        if s.startswith(d):
            return (d, s[len(d):])
    return None

def main():
    parsed = multisplit(["==", "!=", "="], "a!===b=!=c")
    for (a, _, _) in parsed:
        print(a)
    print(parsed)