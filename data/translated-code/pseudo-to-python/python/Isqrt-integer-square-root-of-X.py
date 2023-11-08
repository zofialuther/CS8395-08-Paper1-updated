def isqrt(x):
    q = 1
    while q <= x:
        q *= 4
    z = x
    r = 0
    while q > 1:
        q /= 4
        t = z - r - q
        r = r / 2
        if t >= 0:
            z = t
            r = r + q
    return r

print(' '.join( '%d' % isqrt(n) for n in range(66)))
print('\n'.join( '{0:114,} = isqrt(7^{1:3})'.format(isqrt(7**n), n) for n in range(1, 204, 2)))