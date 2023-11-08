def mult(a, b):
    if len(a) == 0:
        return [[0]]
    if len(a[0]) != len(b):
        return None  # invalid dims

    n = len(a[0])
    m = len(a)
    p = len(b[0])

    ans = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                ans[i][j] += a[i][k] * b[k][j]

    return ans