def options(lo, hi, total):
    ds = list(range(lo, hi+1))
    result = [(x, y, z)
              for x in filter(lambda x: x % 2 == 0, ds)
              for y in filter(lambda y: y != x, ds)
              if lo <= (z := total - (x + y)) <= hi and y != z]
    return result