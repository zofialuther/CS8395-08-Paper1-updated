def spiral(n):
    dat = [[None for i in range(n)] for j in range(n)]
    le = sum([[i + 1, i + 1] for i in reversed(range(n))], [])[1:]
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]] * ((len(le) + 4) // 4)
    x = -1
    y = 0
    val = -1
    for steps, (dx, dy) in zip(le, dxdy):
        x = x + dx
        y = y + dy
        val = val + 1
        for j in range(steps):
            dat[y][x] = val
            if j != steps - 1:
                x = x + dx
                y = y + dy
                val = val + 1
    return dat

for row in spiral(5):
    print(' '.join('%3s' % x for x in row))