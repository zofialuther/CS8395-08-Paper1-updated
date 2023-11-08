def hailstone(n):
    X = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        X.append(n)
    return X

print(length([27, 82, 41, 124]))  # 112

print(append([27, 82, 41, 124], []))  # [27, 82, 41, 124]

print(append([], [8, 4, 2, 1]))  # [8, 4, 2, 1]