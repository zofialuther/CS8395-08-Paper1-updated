def hailstone(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n

max_length = 0
max_num = 0
for i in range(1, 100000):
    length = len(list(hailstone(i)))
    if length > max_length:
        max_length = length
        max_num = i

print(max_num)