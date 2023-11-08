def options(lo, hi, total):
    ds = list(range(lo, hi+1))
    result = []
    for x in ds:
        if x % 2 == 0:
            for y in ds:
                if y != x:
                    z = total - (x + y)
                    if y != z and lo <= z and z <= hi:
                        result.append((x, y, z))
    return result