def agm(a, g):
    a1 = a
    g1 = g
    while abs(a1 - g1) >= 1.0e-14:
        arith = (a1 + g1) / 2.0
        geom = (a1 * g1)**0.5
        a1 = arith
        g1 = geom
    return a1

print(agm(1.0, 1.0 / (2.0)**0.5))