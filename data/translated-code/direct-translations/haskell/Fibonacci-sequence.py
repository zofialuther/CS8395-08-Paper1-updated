def f(n, ab):
    a, b = ab
    return (2 * n, (a * a + b * b, 2 * a * b + b * b))

result = (1, (0, 1))
for _ in range(b):
    result = f(result[0], result[1])

print(result[1][1])