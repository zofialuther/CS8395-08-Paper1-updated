from sympy import primerange

type Result = [(str, [int])]

oneMillionPrimes = list(primerange(2, 1000000))

def getGroups(ps):
    if not ps:
        return []
    n, x, y, *rest = ps
    if x - n == 6 and y - x == 4 and rest and rest[0] - y == 2:
        return [("(6 4 2)", [n, x, y, rest[0])] + getGroups(rest[1:])
    elif x - n == 4 and y - x == 2:
        return [("(4 2)", [n, x, y])] + getGroups(rest)
    elif x - n == 2 and y - x == 4:
        return [("(2 4)", [n, x, y]), ("2", [n, x])] + getGroups(rest)
    elif x - n == 2 and y - x == 2:
        return [("(2 2)", [n, x, y]), ("2", [n, x])] + getGroups(rest)
    elif x - n == 2:
        return [("2", [n, x])] + getGroups(rest)
    elif x - n == 1:
        return [("1", [n, x])] + getGroups(rest)
    else:
        return getGroups(rest)

groups = getGroups(oneMillionPrimes)

def showGroup(group):
    r = [b for a, b in groups if a == group]
    print(f"Differences of {group}: {len(r)}")
    print(f"First: {r[0]}\nLast: {r[-1]}\n")

showGroup("2")
showGroup("1")
showGroup("(2 2)")
showGroup("(2 4)")
showGroup("(4 2)")
showGroup("(6 4 2)")