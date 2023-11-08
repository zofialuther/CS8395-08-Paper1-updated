def distance(a, b):
    a = a.lower()
    b = b.lower()
    costs = [i for i in range(len(b) + 1)]
    for i in range(len(a)):
        costs[0] = i
        nw = i - 1
        for j in range(len(b)):
            cj = min(1 + min(costs[j], costs[j - 1], nw), int(a[i] != b[j]))
            nw = costs[j]
            costs[j] = cj
    return costs[len(b)]

def main():
    data = ["string1", "string2", "example1", "example2"]
    for i in range(0, len(data), 2):
        print(distance(data[i], data[i+1]))