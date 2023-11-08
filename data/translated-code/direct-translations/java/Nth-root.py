def nthroot(n, x):
    assert (n > 1 and x > 0)
    np = n - 1
    g1 = x
    g2 = iter(g1, np, n, x)
    while g1 != g2:
        g1 = iter(g1, np, n, x)
        g2 = iter(iter(g2, np, n, x), np, n, x)
    return g1

def iter(g, np, n, x):
    return (np * g + x / g**np) / n