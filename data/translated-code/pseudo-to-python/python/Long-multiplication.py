def longmult(x, y):
    return reduce(digitSum, polymul(digits(x), digits(y)), 0)

def digitSum(a, x):
    return a * 10 + x

def polymul(xs, ys):
    return list(map(lambda *vs: sum(filter(None, vs)), *[ [0] * i + zs for i, zs in enumerate(mult_table(xs, ys)) ]))

def mult_table(xs, ys):
    return [[x * y for x in xs] for y in ys]

def digits(x):
    return [int(c) for c in str(x)]

if __name__ == '__main__':
    print(longmult(2 ** 64, 2 ** 64))