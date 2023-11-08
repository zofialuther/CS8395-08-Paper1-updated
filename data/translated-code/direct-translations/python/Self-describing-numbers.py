def isSelfDescribing(n):
    s = str(n)
    return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))

self_describing_numbers = [x for x in range(4000000) if isSelfDescribing(x)]
print(self_describing_numbers)

results = [(x, isSelfDescribing(x)) for x in (1210, 2020, 21200, 3211000, 42101000, 521001000, 6210001000)]
print(results)