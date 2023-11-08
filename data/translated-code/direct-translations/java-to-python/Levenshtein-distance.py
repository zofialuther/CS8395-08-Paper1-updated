def distance(a, b):
    a = a.lower()
    b = b.lower()
    costs = [j for j in range(len(b) + 1)]
    for i in range(1, len(a) + 1):
        costs[0] = i
        nw = i - 1
        for j in range(1, len(b) + 1):
            cj = min(1 + min(costs[j], costs[j - 1]), nw if a[i - 1] == b[j - 1] else nw + 1)
            nw = costs[j]
            costs[j] = cj
    return costs[len(b)]

data = [ "kitten", "sitting", "saturday", "sunday", "rosettacode", "raisethysword" ]
for i in range(0, len(data), 2):
    print("distance(" + data[i] + ", " + data[i+1] + ") = " + str(distance(data[i], data[i+1])))