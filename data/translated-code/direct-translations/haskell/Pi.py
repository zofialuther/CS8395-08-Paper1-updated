def g(q, r, t, k, n, l):
    if 4 * q + r - t < n * t:
        return [n] + g(10 * q, 10 * (r - n * t), t, k, (10 * (3 * q + r)) // t - 10 * n, l)
    else:
        return g(q * k, (2 * q + r) * l, t * l, k + 1, (q * (7 * k + 2) + r * l) // (t * l), l + 2)

pi_ = g(1, 0, 1, 1, 3, 3)