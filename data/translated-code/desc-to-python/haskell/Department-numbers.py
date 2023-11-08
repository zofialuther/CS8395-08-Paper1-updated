def options(lo, hi, total):
    num_list = [i for i in range(lo, hi+1)]
    result = [(x, y, total - x - y) for x in num_list if x % 2 == 0
              for y in num_list if y != x and y != total - x - y and lo <= total - x - y <= hi]
    return result