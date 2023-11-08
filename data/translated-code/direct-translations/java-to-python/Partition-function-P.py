from datetime import datetime

def partitions(n):
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n + 1):
        p[i] = 0
        k = 1
        while True:
            j = (k * (3 * k - 1)) // 2
            if j > i:
                break
            if k % 2 != 0:
                p[i] += p[i - j]
            else:
                p[i] -= p[i - j]
            k += 1
            j = k
            if j > i:
                break
            if k % 2 != 0:
                p[i] += p[i - j]
            else:
                p[i] -= p[i - j]
    return p[n]

start = datetime.now()
result = partitions(6666)
end = datetime.now()
print(f"P(6666) = {result}")
print(f"elapsed time: {end - start}")