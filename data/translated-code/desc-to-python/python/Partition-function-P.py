def posd(n):
    return n * (3 * n - 1) // 2

def pos_gen():
    n = 0
    while True:
        n += 1
        yield n * (3 * n - 1) // 2

def plus_minus(k):
    if (k % 4 < 2):
        return k // 2 + 1, 1
    else:
        return -(k // 2 + 1), -1

def part(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for k in range(1, n + 1):
        offset, sign = plus_minus(k)
        for i in range(offset, n + 1):
            partitions[i] += sign * partitions[i - posd(k)]
    return partitions[n]

for i in range(10):
    print(part(i))